def generate_answer(query, retrieved_chunks):
    answer = ""
    for chunk in retrieved_chunks:
        if query.lower() in chunk.lower():
            answer += chunk + "\n"
    return answer