import openai

openai.api_key = "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"

def handle_message(update, bot):
    text = update.message.text
    user = update.message.chat.id

    prompt = f"Bạn là ChemBuddy - trợ lý AI học Hóa. Trả lời ngắn gọn, rõ ràng. Câu hỏi: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Bạn là ChemBuddy - trợ lý AI chuyên dạy Hóa học THPT."},
            {"role": "user", "content": text}
        ]
    )
    answer = response['choices'][0]['message']['content']
    bot.send_message(chat_id=user, text=answer)
