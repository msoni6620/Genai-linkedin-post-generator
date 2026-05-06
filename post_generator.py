from llm_helper import llm
from few_shot import FewShotPosts

few_shot=FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    
def generate_post(length,language,tag):
    prompt=get_prompt(length,language,tag)
    response=llm.invoke(prompt)
    return response.content
    
def get_prompt(length,language,tag):
    length_str=get_length_str(length)

    prompt=f'''
    Generate a LinkedIn post using the following inputs.

    Instructions:
    1. Return only the post content. Do not include any explanation or preamble.
    2. Topic: {tag}
    3. Length: {length_str} (Short: 3–5 lines, Medium: 6–10 lines, Long: 10–15 lines)
    4. Language: {language}

    Language Rules:
    - If language = "English", write fully in English.
    - If language = "Hinglish", write a mix of Hindi and English words, but use only English (Latin) script. Do not use Devanagari script.

    Content Guidelines:
    - Start with a strong hook (first line should grab attention).
    - Keep tone natural and human-like (avoid robotic/AI tone).
    - Use short lines and proper spacing for readability.
    - Optionally include 1–2 emojis (not excessive).
    - End with a clear takeaway or engaging closing line.
    - Do not include hashtags.

    Output:
    Return only the final LinkedIn post as plain text.

'''
    example=few_shot.get_filtered_posts(length,language,tag)
    if len(example)>0:
        prompt+="5) Use writing style as per the following examples."
    for i, post in enumerate(example):
        post_text=post['text']
        prompt+=f'\n\n Example {i+1}: \n\n {post_text}'

        if i==1:
            break
    return prompt

if __name__=="__main__":
    '''print(generate_post("Medium","Hinglish","Motivation"))'''