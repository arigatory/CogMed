from aiogram.dispatcher.filters.state import StatesGroup, State


class MedicalCardStates(StatesGroup):
    Q1 = State()
    Q1_1 = State()
    Q1_2 = State()
    Q1_3 = State()
    Q1_4 = State()
    Q2 = State()
    Q2_1 = State()
    Q2_1_1 = State()
    Q2_1_2 = State()
    Q2_2 = State()
    Q2_3 = State()
    Q2_3_1 = State()
    Q2_3_2 = State()
    Q2_4 = State()
    Q2_4_1 = State()
    Q2_4_2 = State()
    Q2_4_3 = State()
    Q2_5 = State()
    Q2_6 = State()
    Q3 = State()
    Q3_1 = State()
    Q3_2 = State()
    Q3_3 = State()
    Q3_4 = State()
    Q3_4_1 = State()
    Q3_4_2 = State()


class RemindStates(StatesGroup):
    GetRemindState = State()
