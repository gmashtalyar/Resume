import streamlit as st
from pathlib import Path
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "Resume_Mashtalyar.pdf"

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

image = Image.open('photo.png')

col1, col2, col3 = st.columns(3, gap='small')
with col1:
    st.image(image, width=150)
with col2:
    # st.title("Машталяр Геннадий")
    st.download_button(
        label=" 📄 Скачать резюме",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📫", "gmashtalyar@yandex.ru")
    st.write("+7 916 979-8743")
with col3:
    st.write("")



st.markdown('## Сводка', unsafe_allow_html=True)
st.info('''
- С недавнего времени выступаю на конференциях CFO-Russia (управление ДЗ, управление ликвидностью).
- 7-летний опыт извлечения полезных идей из данных.
- Сильный опыт в построении финансовых моделей в Excel и Python. 
- Хорошее понимание статистических принципов и их соответствующих применений.
- Отличный командный игрок, проявляю инициативу при выполнении задач.

''')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Машталяр Геннадий</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Главная <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Образование</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Опыт работы</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Навыки</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#links">Ссылки</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'{a}')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'{a}')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

st.markdown('''
## Education
''')

txt('**Магистратура по финансам |**  [Hult International School of Business](https://www.hult.edu/masters/finance/), Лондон',
'2015-2016')

st.markdown('''
- `Победитель` консалтингового проекта по факторингу для [Advance Global Capital](https://advanceglobalcap.com).
''')

txt('**Бакалавр по финансам |**  [The university of Tampa](https://www.ut.edu/academics/sykes-college-of-business/finance-degree), Флорида', '2012-2015')

st.markdown('''
- `Топ-15%` на ГОС экзамене
- Сертифицированный SAP Специалист
- `4-е` место по курсовой работе
''')

st.markdown('''
## Experience
''')

txt('**Бизнес аналитик |**  [Ариэль Металл](https://arielmetal.ru)', '2021-2023')
st.markdown('''
Металлотрейдер с выручкой `~20 млрд.р.` и оборотом +`350` т.тн.
- Постоение бизнес-плана компании с участием кросс-функциональных отделов (продажи, склад, логистика, финансы, персонал).
- Автоматизаия отчетности с помощью `Python`, ad-hoc отчеты в `Streamlit`.
- Анализ бизнес-показателей и их сопоставление с текущей деятельностью.
- Построение модели управления закупками, складскими запасами и продажами.
- Формирование управленческой отчетности, прогнозной, сценарной отчетности для руководства; отображение онлайн отчености в `Qlik Sense`.
- Разработка финансовых моделей для оценки инвестиционныз возможностей (`DCF, NPV, IRR`).
- Создание `Django` приложения для кредитного комитета с `api-подключением` к Контур-Фокусу.
''')

txt('**Директор по развитию |** [КСК-Фактор](https://ksk-factor.ru)', '2018-2021')
st.markdown('''
Факторинговая компания с портфелем +`700` млн.р. Работа по повышению эффективности компании. Развитие новых стратегических направлений компании. Запуск новых продуктов, построение сотрудничества с Точка банком.
* Риск менеджмент - операционного и кредитного риска по +`100` клиентам (МСБ) и +`50` дебиторам (РБК500).
  * Принял участие на кредитном комитете в +`50` структурных долговых сделках с размером +`10` млн.р.
  * Кредитный анализ дебиторов и их поставщиков. 
  * Ежедневный анализ реализации операционного риска.
* Казначейские операции - управление финансовыми транзакциями компании с оборотами по счетам + `10 млрд.р`.
  * Разработал систему прогнозирования портфеоя с дюрацией `30` дней для управления ежедневной ликвидностью.
  * Участие в привлечении кредитного капитала компании +`300` млн.р.
  * Контроль кредитных ковенант и выборка кредитных траншей.
  * Управление операционным бюджетом.
* Формирование отчетности - построение прогнозной и фактической отчетности для руководства. 
  * Разработка финансовых моделей для оценки инвестиционных возможностей (`DCF, NPV, IRR`).
  * Составление управленческой отчености (P&L, BS, CF).
''')

txt('**Финансовый консультант**', '2016-2023')
st.markdown('''
Консультировал ряд крупных и малых бизнес-проектов по вопросам финансового моделирования действующих бизнес-проектов и их оценки.
* Совкомбанк - построил финансовую модель Private Bank'a после `M&A` Росевробанка.
* Авто-стартапы (продажа, аренда, лизинг) - строил финансовые модели для ряда стартап проектов (`LTV, CAC, unit-econometrics`).
''')

txt('**Старший аналитик |**  Министрерство Спорта', '2017-2018')
st.markdown('''
Аналитик в отеделе по строительствую `7/8` стадионов и инфраструктуры стоимостью +`1 трлн.р.` для Чемпионата мира по футболу 2018 года.
* Формирование финансовой отчетности для руководства и государственноых органов (ФНС, Счетная палата, Росимущество и пр.)
* Анализ потенциала коммерческого использования стадионов после ЧМ2018.
* Формирование и контроль операционного бюджета.
''')

txt('**Младший аналитик |**  [Ernst&Young | финансовое моделирование](https://www.ey.com/en_gl/strategy-transactions/valuation-modeling-economics)', '2016-2017')
st.markdown('''
Участвовал в консультационных проектах по оценке бизнеса и финансовому моделированию.
* Разработка финансовых моделей, оценка компаний и активов.
* Разработка визуализации данных через `Spotfire`.
* Работа с базами данных через `SQL & Access`.
* Создание web-проекта (`Javascript, C#, HTML&CSS, SQL`) в рамках внутренних задач компании.
''')


st.markdown('''
## Skills
''')
txt3('Программирование', '`Python`, `Javascript`, `Java`.')
txt3('Работа в программах', '`SAP`, `Eviews`, `Spotfire`, `FactSet`.')
txt3('Обработка данных', '`SQL`, `Pandas`, `numpy`.')
txt3('Моделирование', '`MonteCarlo Simulations`, `linear regressions`, `decision trees`')
txt3('Базы данных', '`SQLite3`')
txt3('Визуализация данных', '`QlikSense`, `matplotlib`, `ChartJS`, `Streamlit`.')
txt3('Web-разработка', '`Django`, `Spring`, `HTML`, `CSS`.')
txt3('Иностранные языки', '`Английский`, `Шведский`, `Французский`.')


st.markdown('''
## Links
''')

txt2('`GitHub`', 'https://github.com/gmashtalyar')




