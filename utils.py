from transformers import pipeline

def generate_copywriting(detections):
    # Example: simple template-based generation
    text_generator = pipeline('text-generation', model='gpt-2')
    detected_objects = ", ".join([f"Object {d['class']}" for d in detections])
    prompt = f"The video shows the following objects: {detected_objects}. Write a short social media post about this."
    
    result = text_generator(prompt, max_length=50)
    return result[0]['generated_text']