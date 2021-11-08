from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove


from loader import dp
from aiogram import types

from models.medical_card import MedicalCard
from states import MedicalCardStates
import fpdf
import os


questions = {
    1: "Фамилия Имя Отчество:",
    2: "Дата рождения",
    3: "Пол:",
    4: "Примерный Рост и Вес",
    5: "что беспокоит больше всего/ причина обращения/ведущий симптом/жалоба:",
    6: "Когда начало беспокоить:",
    7: "Как долго беспокоит:",
    8: "Как изменяется с течением времени (стало беспокоить сильнее, слабоее, беспокоит точно также):",
    9: "Аллергии на что либо, непереносимость чего либо:",
    10: "Ставили какие-либо диагнозы в течение жизни/ переносили какие либо операции?:",
    11: "Проходили недавно какие -либо исследования (МРТ, КТ, генетические исследования, анализы крови, исследования нервов, дыхания, желудка, кишечника, костей, щитовидной железы, печени, мочеполовых органов..):",
    12: "В семье кто-то чем-то болеет (только кровные родственники):",
    13: "Проживаете 1 или с кем-то?:",
    14: "Где работаете/работали/на пенсии:",
    15: "Инвалидность имеется или нет?:",
    16: "Что то принимаете на постоянной основе (препараты, отвары, настои, мази, крема, свечи, травы)"
}


class MyPDF(fpdf.FPDF):
    def __init__(self, m):
        super().__init__()
        self.message = m
    """"""
    # ----------------------------------------------------------------------
    def header(self):
        """
        Header on each page
        """
        # set the font for the header, B=Bold
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        # insert my logo
        self.image(r"C:\Users\ariga\1med\bot\1medbot\logo.jpg", x=10, y=8, w=23)
        # position logo on the right
        self.cell(w=80)
        title = f"Медицинская карта пользователя {self.message.from_user.first_name}"
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

        # page title
        self.cell(200, 20, txt=f"Данные telegram: ({self.message.from_user.username}, id:{self.message.from_user.id})", border=0, ln=1, align="C")

        # insert a line break of 20 pixels
        self.ln(20)

    def chapter_title(self, num, label):
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Вопрос %d : %s' % (num, label), 0, 1, 'L', True)
        # Line break
        self.ln(4)


    # ----------------------------------------------------------------------
    def footer(self):
        """
        Footer on each page
        """
        # position footer at 15mm from the bottom
        self.set_y(-15)

        # set the font, I=italic
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 14)
        # display the page number and center it
        pageNum = "Страница %s/{nb}" % self.page_no()
        self.cell(0, 10, pageNum, align="C")


@dp.message_handler(text='📚 Медицинская карта')
async def enter_medical_card(message: types.Message):
    await message.answer("Начинаем заполнять медицинскую карту:\n"
                         "✔️Вопрос №1\n\n" + questions[1], reply_markup=ReplyKeyboardRemove())
    await MedicalCardStates.Q1_FIO.set()


@dp.message_handler(state=MedicalCardStates.Q1_FIO)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    medical_card = MedicalCard(message.from_user.id)
    medical_card.answers[1] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №2\n\n" + questions[2])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q2_FIO)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[2] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №3\n\n" + questions[3])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q3_FIO)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[3] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №4\n\n" + questions[4])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q4_FIO)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[4] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №5\n\n" + questions[5])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q5_FIO)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[5] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №6\n\n" + questions[6])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q6_FIO)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[6] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №7\n\n" + questions[7])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q7_FIO)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[7] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №8\n\n" + questions[8])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q8_FIO)
async def answer_q8(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[8] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №9\n\n" + questions[9])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q9_FIO)
async def answer_q9(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[9] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №10\n\n" + questions[10])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q10_FIO)
async def answer_q10(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[10] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №11\n\n" + questions[11])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q11_FIO)
async def answer_q11(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[11] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №12\n\n" + questions[12])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q12_FIO)
async def answer_q12(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[12] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №13\n\n" + questions[13])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q13_FIO)
async def answer_q13(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[13] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №14\n\n" + questions[14])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q14_FIO)
async def answer_q14(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[14] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №15\n\n" + questions[15])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q15_FIO)
async def answer_q15(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[15] = answer
    await state.update_data(medical_card=medical_card)
    await message.answer("✔️Вопрос №16\n\n" + questions[16])
    await MedicalCardStates.next()


@dp.message_handler(state=MedicalCardStates.Q16_FIO)
async def answer_q15(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    medical_card: MedicalCard = data.get("medical_card")
    medical_card.answers[16] = answer
    await state.update_data(medical_card=medical_card)
    await state.finish()
    await message.answer("Cпасибо за ответы")
    pdf = MyPDF(message)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    for key in questions:
        pdf.chapter_title(key, questions[key])
        pdf.cell(200, 10, txt=f"Ответ: {medical_card.answers[key]}", ln=1, align="L")
    path_name = f"medical_card_{message.from_user.username}_{message.from_user.id}_date_{datetime.now().strftime('%Y%m%d-%H%M%S')}.pdf"
    pdf.output(path_name)
    doc = open(path_name, 'rb')
    await dp.bot.send_document(message.chat.id, doc)
    await dp.bot.sen
    doc.close()
