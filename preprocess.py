import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def extract_metadata(post):
     template='''
     You are given a LinkedIn post. Your task is to extract structured information from it.

     Instructions:
     1. Return ONLY a valid JSON object. Do not include any explanation, text, or preamble.
     2. The JSON object must contain exactly three keys:
     - "line_count": integer (number of lines in the post, count based on newline characters)
     - "language": string ("English" or "Hinglish")
     - "tags": array of strings (maximum 2 relevant tags)

     Rules:
     - Count lines based on line breaks (\n). If no line breaks exist, line_count = 1.
     - "Hinglish" means a mix of Hindi and English words written in Latin script.
     - Tags should be short, meaningful keywords based on the main topic (e.g., "AI", "Career", "Motivation").
     - Do not generate more than 2 tags.
     - Do not include duplicate tags.
     - Ensure the output is valid JSON (double quotes, proper commas, no trailing commas).

     Input Post:
{post}
'''
     pt=PromptTemplate.from_template(template)
     chain = pt | llm
     response = chain.invoke(input={"post":post})

     try:
          json_parser=JsonOutputParser()
          res = json_parser.parse(response.content)
     except OutputParserException:
          raise OutputParserException("Context too big. unable to parse jobs.")
     return res
     
def get_unified_tags(posts_with_metadata):
     unique_tags=set()
     #Loop through each post and extract the tags
     for post in posts_with_metadata:
          unique_tags.update(post['tags'])
     
     unique_tags_list = ",".join(unique_tags)
     template='''You are given a list of tags. Your task is to normalize, merge, and map them into a unified set of tags.

     Instructions:
     1. Return ONLY a valid JSON object. Do not include any explanation or extra text.
     2. The output must be a dictionary where:
     - Each key = original tag
     - Each value = unified tag
     3. Similar or related tags must be merged into a single standardized tag.
     - Example: "Jobseekers", "Job Hunting" → "Job Search"
     - Example: "Motivation", "Inspiration", "Drive" → "Motivation"
     - Example: "Personal Growth", "Personal Development", "Self Improvement" → "Self Improvement"
     - Example: "Scam Alert", "Job Scam" → "Scams"
     4. Each unified tag must follow Title Case (e.g., "Job Search", "Self Improvement").
     5. Remove spelling variations, duplicates, and extra spaces before mapping.
     6. Use clear, commonly understood tag names (avoid overly long or vague tags).
     7. Do not create more unique tags than necessary (keep the list concise).
     8. Ensure valid JSON:
     - Use double quotes
     - No trailing commas

     Input Tags:
     {tags}
     '''

     pt = PromptTemplate.from_template(template)
     chain=pt | llm
     response=chain.invoke(input={"tags":str(unique_tags_list)})
     try:
          json_parser=JsonOutputParser()
          res=json_parser.parse(response.content)
     except OutputParserException:
          raise OutputParserException("Context too big. Unable to parse jobs.")
     return res



def process_posts(raw_file_path,processed_file_path="None"):
     with open(raw_file_path,encoding='utf-8') as file:
          posts=json.load(file)
          enriched_posts=[]
          for post in posts:
               metadata=extract_metadata(post['text'])
               post_with_metadata=post | metadata
               enriched_posts.append(post_with_metadata)
          unified_tags =get_unified_tags(enriched_posts)
          for post in enriched_posts:
               current_tags=post['tags']
               new_tags={unified_tags[tag] for tag in current_tags}
               post['tags']=list(new_tags)

          with open(processed_file_path,encoding="utf-8",mode="w") as outfile:
               json.dump(enriched_posts,outfile,indent=4)








if __name__ == "__main__":
     process_posts("data/row_posts.json","data/processed_posts.json")
