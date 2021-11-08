import time
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import doctors, caregivers, patients, menu, red_flags, medications
from keyboards.default.guidlines import guidelines
from keyboards.default.help import help
from keyboards.default.i_feel_bad import i_feel_bad
from keyboards.default.i_lost import i_lost
from keyboards.default.management import management
from keyboards.default.medications import medications
from loader import dp
from aiogram import types

from states import MedicalCardStates

from states.medical_card_states import RemindStates


@dp.message_handler(commands="remind", state="*")
@dp.message_handler(Text(equals="remind", ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await RemindStates.GetRemindState.set()
    await message.answer(f"What do you want to reminded you about?", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=RemindStates.GetRemindState)
async def set_reminder(message: types.Message, state: FSMContext):
    answer = message.text
    await state.finish()
    seconds = 10
    await message.answer(f"I'll remind you about '{answer}' in {seconds} seconds")
    time.sleep(seconds)
    await message.answer(f"{answer}", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Action canceled\nPlease choose who I'm dealing with?", reply_markup=menu)


@dp.message_handler(text='👩‍⚕️ 👨‍⚕️ Doctors')
async def enter_doctors(message: types.Message):
    await message.answer("What would you lime me to do?\n", reply_markup=doctors)
    await MedicalCardStates.Q1.set()


@dp.message_handler(state=MedicalCardStates.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer(f"Here will be {answer}\n", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text='👀 Caregivers')
async def enter_caregivers(message: types.Message):
    await message.answer("What can I help you with?\n", reply_markup=caregivers)
    await MedicalCardStates.Q2.set()


@dp.message_handler(text='👴👵 Patients')
async def enter_patients(message: types.Message):
    await message.answer("What can I help you with?\n", reply_markup=patients)
    await MedicalCardStates.Q3.set()


@dp.message_handler(state=MedicalCardStates.Q2, text="Guidelines")
async def answer_q2(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q2_1.set()
    await message.answer(f"Here are guidelines\n", reply_markup=guidelines)


@dp.message_handler(state=MedicalCardStates.Q2_1, text="Communication rules")
async def answer_q2_1_communication(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Here you can find the main rules for the good communication with the patient.\n", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2_1, text="Living place")
async def answer_q2_1_living(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Here will be the detailed instruction how should you arrange the patients living place.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2, text="Red flags")
async def answer_q2(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q2_3.set()
    await message.answer(f"Here is Red flags menu\n", reply_markup=red_flags)


@dp.message_handler(state=MedicalCardStates.Q2_3, text="Dangerous symptoms")
async def answer_q2_3_dangerous(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Here you can find the most dangerous symptoms that could be observed in a patient. If you see one or more of them you should immediately seek medical advice.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2_3, text="Dangerous adverse effects")
async def answer_q2_3_dangerous(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("If your patient has already got the medication you should be ready to recognize the most dangerous adverse effects. If you see one or more of them you should immediately seek medical advice.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2, text="Management")
async def answer_q2_management(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q2_4.set()
    await message.answer(f"Here is Red flags menu\n", reply_markup=management)


@dp.message_handler(state=MedicalCardStates.Q2_4, text="Tools")
async def answer_q2_4_tools(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("In this section, you can find a piece of information about the specific devices which could support you to take care of the patient.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2_4, text="Rules")
async def answer_q2_4_rules(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Here you can find the main rules for medication use.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2_4)
async def answer_q2_4_rules(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Here will be {message.text} section", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer(f"Here will be {answer}\n", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state=MedicalCardStates.Q3, text="Medications")
async def answer_q2_management(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q3_1.set()
    await message.answer(f"Here is Medications menu\n", reply_markup=medications)


@dp.message_handler(state=MedicalCardStates.Q3_1)
async def answer_q2_4_rules(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Here will be {message.text} section", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q3, text="Help")
async def answer_q2_management(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q3_4.set()
    await message.answer(f"Here is Help menu\n", reply_markup=help)


@dp.message_handler(state=MedicalCardStates.Q3_4, text="I LOST")
async def answer_q3_4_lost(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q3_4_1.set()
    await message.answer(f"Don't be afraid. Just tell me what you want?", reply_markup=i_lost)


@dp.message_handler(state=MedicalCardStates.Q3_4_1)
async def answer_q2_4_rules(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Here will be {message.text} section", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q3_4, text="I FEEL BAD")
async def answer_q3_4_1_lost(message: types.Message, state: FSMContext):
    await MedicalCardStates.Q3_4_2.set()
    await message.answer(f"Here is {message.text} section", reply_markup=i_feel_bad)


@dp.message_handler(state=MedicalCardStates.Q3_4_2)
async def answer_q3_4_2_feel_bad(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Here will be {message.text} section", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q3_4)
async def answer_q3_4_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Here will be {message.text} section", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=MedicalCardStates.Q3)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer(f"Here will be {answer}\n", reply_markup=ReplyKeyboardRemove())
    await state.finish()
