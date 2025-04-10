import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

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
