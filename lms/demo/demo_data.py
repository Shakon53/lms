"""Realistic starter courses installed by the setup wizard.

Generated courses carry a private marker tag so cleanup never touches content
created by a user.
"""

import json

import frappe

from lms.lms.utils import create_user, get_course_progress


DEMO_TAG = "YU-DEMO-2026"
LEGACY_TITLES = ("A guide to YU-LMS", "A guide to Frappe Learning")
DEMO_USERS = ("student.demo@yessenov.edu.kz", "student.two.demo@yessenov.edu.kz")


COURSES = [
	{
		"title": "Цифровая грамотность: уверенная работа с информацией",
		"tags": f"Цифровые навыки, Информационная грамотность, {DEMO_TAG}",
		"color": "Blue",
		"intro": "Научитесь искать, проверять и безопасно использовать информацию в учебе и работе.",
		"description": """<p>Практический курс для студентов любого направления. Вы освоите эффективный поиск, проверку источников, совместную работу с файлами и базовые правила цифровой безопасности.</p><h3>Результаты обучения</h3><ul><li>формулировать точные поисковые запросы;</li><li>оценивать надежность источников;</li><li>защищать аккаунты и персональные данные;</li><li>готовить аккуратные цифровые материалы.</li></ul><p><strong>Формат:</strong> 6 уроков, 2 задания и итоговый тест.</p>""",
		"chapters": [
			("Поиск и оценка информации", [
				("Как устроен цифровой след", "Разберем, какие данные остаются после действий в интернете и как управлять цифровой репутацией.", ["Отделяйте публичные данные от приватных.", "Проверяйте разрешения приложений раз в месяц.", "Не публикуйте документы с персональными данными."]),
				("Поиск без информационного шума", "Освоим операторы поиска, фильтры и приемы уточнения запроса.", ["Используйте кавычки для точной фразы.", "Ограничивайте поиск доменом через site:.", "Сравнивайте дату и контекст публикации."]),
				("Практика: проверка спорной публикации", "assignment", "source_check"),
			]),
			("Безопасность и совместная работа", [
				("Пароли, MFA и фишинг", "Научимся распознавать поддельные письма и защищать аккаунты многофакторной аутентификацией.", ["Используйте уникальные парольные фразы.", "Включайте MFA в важных сервисах.", "Проверяйте домен до перехода по ссылке."]),
				("Файлы и командная работа", "Разберем структуру папок, версии и уровни доступа.", ["Добавляйте дату и версию в имя файла.", "Выдавайте минимально необходимый доступ.", "Храните финальные материалы отдельно от черновиков."]),
				("Практика: цифровой аудит", "assignment", "digital_audit"),
			]),
			("Итоговая аттестация", [("Итоговый тест", "quiz", None)]),
		],
		"assignments": {
			"source_check": ("Проверка надежности источника", "PDF", "Выберите спорную публикацию. Найдите первоисточник, проверьте автора, дату и доказательства, затем подтвердите вывод минимум двумя независимыми источниками. Загрузите отчет на 1–2 страницы.", ["Первоисточник и контекст — 25", "Проверка автора и доказательств — 30", "Независимое подтверждение — 25", "Аргументированный вывод и оформление — 20"]),
			"digital_audit": ("Аудит личной цифровой безопасности", "Text", "Проведите безопасный аудит трех своих аккаунтов: MFA, уникальность паролей, активные сессии и доступ приложений. Не указывайте пароли. Опишите пять улучшений и план на следующий месяц.", ["Полнота аудита — 40", "Конкретные улучшения — 35", "Реалистичный план — 25"]),
		},
		"quiz": [
			("Какой признак сильнее всего повышает надежность материала?", ["Много лайков", "Проверяемый первоисточник", "Яркий заголовок", "Публикация в чате"], 1),
			("Что делать с подозрительным письмом?", ["Открыть вложение", "Ответить", "Проверить домен и связаться по известному каналу", "Переслать коллегам"], 2),
			("Для чего нужна MFA?", ["Ускорить интернет", "Добавить независимое подтверждение входа", "Хранить файлы", "Удалить рекламу"], 1),
			("Какой доступ безопаснее выдать по умолчанию?", ["Публичное редактирование", "Минимально необходимый", "Всем в интернете", "Бессрочный"], 1),
		],
	},
	{
		"title": "Академическое письмо и работа с источниками",
		"tags": f"Академическое письмо, Исследование, {DEMO_TAG}",
		"color": "Violet",
		"intro": "От исследовательского вопроса до ясного текста с корректными ссылками и аргументацией.",
		"description": """<p>Курс помогает подготовить структурированную академическую работу без плагиата. В центре — тезис, доказательства, логика абзаца и ответственное использование источников.</p><h3>Вы научитесь</h3><ul><li>сужать тему до исследовательского вопроса;</li><li>строить аргумент и связный абзац;</li><li>перефразировать без искажения смысла;</li><li>оформлять цитаты и список литературы.</li></ul><p><strong>Итог:</strong> готовый фрагмент академической работы и тест.</p>""",
		"chapters": [
			("Аргумент и структура", [
				("От темы к исследовательскому вопросу", "Хороший вопрос конкретен, исследуем и допускает аргументированный ответ.", ["Ограничьте объект, период и контекст.", "Избегайте вопросов с ответом «да» или «нет».", "Проверьте доступность источников."]),
				("Тезис и логика абзаца", "Освоим модель: тезис — доказательство — объяснение — вывод.", ["Один абзац раскрывает одну мысль.", "Каждое доказательство связывайте с тезисом.", "Переходы показывают логику рассуждения."]),
				("Практика: карта аргумента", "assignment", "argument_map"),
			]),
			("Источники и академическая этика", [
				("Цитирование, пересказ и плагиат", "Разберем, когда цитировать дословно, когда пересказывать и почему ссылка нужна в обоих случаях.", ["Сохраняйте смысл автора.", "Отмечайте прямые цитаты кавычками.", "Фиксируйте источник сразу."]),
				("Редактирование ясного текста", "Проверим текст на точность, связность и единообразие терминов.", ["Сначала редактируйте структуру.", "Заменяйте расплывчатые слова конкретными.", "Читайте текст вслух."]),
				("Практика: аналитический абзац", "assignment", "academic_paragraph"),
			]),
			("Итоговая аттестация", [("Итоговый тест", "quiz", None)]),
		],
		"assignments": {
			"argument_map": ("Карта академического аргумента", "PDF", "Сформулируйте исследовательский вопрос и тезис. Подготовьте карту из двух аргументов, возможного контраргумента и ответа на него. Для каждого аргумента укажите тип доказательств.", ["Вопрос и тезис — 30", "Логика аргументов — 35", "Контраргумент — 20", "Выбор доказательств — 15"]),
			"academic_paragraph": ("Аналитический абзац с источниками", "Document", "Напишите 180–250 слов: тезисное предложение, данные из двух надежных источников, объяснение связи доказательств с тезисом и итоговое предложение. Добавьте ссылки в одном стиле.", ["Ясный тезис — 20", "Интеграция источников — 30", "Анализ — 30", "Связность и оформление — 20"]),
		},
		"quiz": [
			("Какой исследовательский вопрос лучше?", ["Что такое образование?", "Как смешанное обучение повлияло на вовлеченность первокурсников YU в 2025 году?", "Полезен ли интернет?", "Почему всё меняется?"], 1),
			("Что следует за доказательством в аналитическом абзаце?", ["Несвязанная мысль", "Объяснение связи с тезисом", "Длинная цитата", "Список терминов"], 1),
			("Нужна ли ссылка при пересказе идеи?", ["Нет", "Только в заключении", "Да, источник идеи нужно указать", "Только для длинного текста"], 2),
			("С чего начинать редактирование?", ["С запятых", "Со структуры и логики", "Со шрифта", "С нумерации"], 1),
		],
	},
	{
		"title": "Управление проектами: от идеи до результата",
		"tags": f"Проекты, Командная работа, {DEMO_TAG}",
		"color": "Teal",
		"intro": "Спланируйте учебный или рабочий проект: цель, роли, сроки, риски и измеримый результат.",
		"description": """<p>Прикладной курс по запуску небольших проектов. Вы создадите паспорт проекта, рабочий план и реестр рисков.</p><h3>После курса вы сможете</h3><ul><li>ставить измеримую цель и определять границы;</li><li>декомпозировать результат на задачи;</li><li>распределять ответственность;</li><li>управлять сроками, рисками и изменениями.</li></ul><p><strong>Формат:</strong> теория, шаблоны, две работы и итоговый тест.</p>""",
		"chapters": [
			("Запуск проекта", [
				("Цель, результат и границы", "Различим проблему, цель, продукт проекта и критерии готовности.", ["Формулируйте цель через результат.", "Зафиксируйте, что не входит в проект.", "Согласуйте критерии приемки до старта."]),
				("Заинтересованные стороны и роли", "Определим заказчика, пользователей, команду и зоны ответственности.", ["У каждой задачи один ответственный.", "Вовлекайте пользователей заранее.", "Фиксируйте решения."]),
				("Практика: паспорт проекта", "assignment", "project_charter"),
			]),
			("Планирование и контроль", [
				("Декомпозиция, сроки и зависимости", "Разобьем результат на проверяемые задачи и построим реалистичную последовательность.", ["У задачи должен быть результат.", "Отмечайте зависимости до сроков.", "Оставляйте резерв."]),
				("Риски и ретроспектива", "Создадим реестр рисков и ритм коротких статусных встреч.", ["Оценивайте вероятность и влияние.", "Назначайте владельца реакции.", "Завершайте этап разбором уроков."]),
				("Практика: план и реестр рисков", "assignment", "risk_plan"),
			]),
			("Итоговая аттестация", [("Итоговый тест", "quiz", None)]),
		],
		"assignments": {
			"project_charter": ("Паспорт проекта", "PDF", "Подготовьте одностраничный паспорт проекта: проблема, SMART-цель, измеримый результат, границы, заинтересованные стороны, роли и три критерия приемки.", ["Проблема и цель — 30", "Результат и границы — 25", "Роли — 25", "Критерии приемки — 20"]),
			"risk_plan": ("План работ и реестр рисков", "Document", "Разбейте проект минимум на 8 задач, укажите ответственных, сроки и зависимости. Добавьте 5 рисков с вероятностью, влиянием, профилактикой и планом реакции.", ["Декомпозиция — 30", "Сроки и зависимости — 25", "Анализ рисков — 30", "Ясность документа — 15"]),
		},
		"quiz": [
			("Что описывает критерий приемки?", ["Настроение команды", "Проверяемое условие готовности", "Бюджет вуза", "Название проекта"], 1),
			("Зачем фиксировать границы проекта?", ["Исключить команду", "Управлять ожиданиями и изменениями", "Не оценивать сроки", "Убрать качество"], 1),
			("Что сделать до назначения сроков?", ["Выбрать цвет", "Определить зависимости", "Закрыть проект", "Удалить риски"], 1),
			("Хорошая запись о риске включает…", ["Только название", "Вероятность, влияние, владельца и реакцию", "Только стоимость", "Список участников"], 1),
		],
	},
]


def create_demo_data(args: dict | None = None):
	remove_legacy_demo_content()
	instructor = get_or_create_instructor()
	students = get_or_create_students()
	for index, spec in enumerate(COURSES):
		course = create_course(spec, instructor)
		create_course_content(course, spec)
		for student in students:
			enroll(student, course)
		create_progress(course, students[0], 2 + index)
	frappe.db.set_single_value("LMS Settings", "demo_data_present", 1)


def remove_legacy_demo_content():
	from lms.lms.api import delete_course

	legacy = frappe.get_all("LMS Course", {"title": ["in", LEGACY_TITLES]}, pluck="name")
	generated = frappe.get_all("LMS Course", {"tags": ["like", f"%{DEMO_TAG}%"]}, pluck="name")
	for name in dict.fromkeys([*legacy, *generated]):
		assignments = frappe.get_all("LMS Assignment", {"course": name}, pluck="name")
		quizzes = frappe.get_all("LMS Quiz", {"course": name}, pluck="name")
		questions = (
			frappe.get_all("LMS Quiz Question", {"parent": ["in", quizzes]}, pluck="question")
			if quizzes
			else []
		)
		delete_course(name)
		for assignment in assignments:
			frappe.delete_doc("LMS Assignment", assignment, ignore_permissions=True)
		for quiz in quizzes:
			frappe.delete_doc("LMS Quiz", quiz, ignore_permissions=True)
		for question in questions:
			if frappe.db.exists("LMS Question", question):
				frappe.delete_doc("LMS Question", question, ignore_permissions=True)
	frappe.db.delete("LMS Quiz", {"title": "Do you know YU-LMS?"})
	for email in ("ash@ipp.com", "john.doe@example.com", "jane.smith@example.com", "jannat@example.com"):
		has_courses = frappe.db.exists("Course Instructor", {"instructor": email})
		has_enrollments = frappe.db.exists("LMS Enrollment", {"member": email})
		if frappe.db.exists("User", email) and not has_courses and not has_enrollments:
			frappe.delete_doc("User", email, ignore_permissions=True)


def get_or_create_instructor():
	users = frappe.get_all("User", {"name": ["not in", ("Administrator", "Guest", *DEMO_USERS)]}, pluck="name", limit=1)
	if users:
		user = frappe.get_doc("User", users[0])
		user.add_roles("Moderator")
		return user
	return create_user(email="instructor.demo@yessenov.edu.kz", first_name="Преподаватель", last_name="YU", full_name="Преподаватель Yessenov University", roles=["Moderator"])


def get_or_create_students():
	return [
		create_user(email=DEMO_USERS[0], first_name="Айдана", last_name="Серик", full_name="Айдана Серик"),
		create_user(email=DEMO_USERS[1], first_name="Данияр", last_name="Омаров", full_name="Данияр Омаров"),
	]


def create_course(spec, instructor):
	doc = frappe.new_doc("LMS Course")
	doc.update({"title": spec["title"], "category": "Business", "tags": spec["tags"], "card_gradient": spec["color"], "published": 1, "featured": 1, "enable_certification": 1, "short_introduction": spec["intro"], "description": spec["description"], "instructors": [{"instructor": instructor.name}]})
	doc.save()
	return doc


def create_course_content(course, spec):
	assignments = {key: create_assignment(course, value) for key, value in spec["assignments"].items()}
	quiz = create_quiz(course, spec["quiz"])
	for chapter_title, lessons in spec["chapters"]:
		chapter = frappe.get_doc({"doctype": "Course Chapter", "course": course.name, "title": chapter_title}).insert()
		course.append("chapters", {"chapter": chapter.name})
		for lesson_spec in lessons:
			if lesson_spec[1] == "quiz":
				content = assessment_content("quiz", "quiz", quiz.name)
			elif lesson_spec[1] == "assignment":
				content = assessment_content("assignment", "assignment", assignments[lesson_spec[2]].name)
			else:
				content = lesson_content(lesson_spec[1], lesson_spec[2])
			lesson = frappe.get_doc({"doctype": "Course Lesson", "course": course.name, "chapter": chapter.name, "title": lesson_spec[0], "content": content}).insert()
			chapter.append("lessons", {"lesson": lesson.name})
		chapter.save()
	course.save()


def lesson_content(introduction, points):
	blocks = [{"type": "paragraph", "data": {"text": introduction}}, {"type": "header", "data": {"text": "Ключевые идеи", "level": 2}}, {"type": "list", "data": {"style": "unordered", "items": [{"content": point, "items": []} for point in points]}}, {"type": "header", "data": {"text": "Проверьте себя", "level": 3}}, {"type": "paragraph", "data": {"text": "Сформулируйте одним предложением, как примените материал в ближайшей задаче."}}]
	return json.dumps({"time": 1790294400000, "blocks": blocks, "version": "2.29.0"}, ensure_ascii=False)


def assessment_content(block_type, field, name):
	return json.dumps({"time": 1790294400000, "blocks": [{"type": block_type, "data": {field: name}}], "version": "2.29.0"})


def create_assignment(course, spec):
	title, file_type, question, rubric = spec
	doc = frappe.new_doc("LMS Assignment")
	doc.update({"title": title, "course": course.name, "type": file_type, "question": f"<p>{question}</p>", "grading_rubric": "<ul>" + "".join(f"<li>{item} баллов</li>" for item in rubric) + "</ul>", "maximum_score": 100, "grade_assignment": 1})
	doc.save()
	return doc


def create_quiz(course, questions):
	quiz = frappe.new_doc("LMS Quiz")
	quiz.update({"title": f"Итоговый тест — {course.title}", "course": course.name, "passing_percentage": 75, "max_attempts": 3, "duration": "15", "show_answers": 1, "show_submission_history": 1})
	for text, options, correct in questions:
		question = frappe.new_doc("LMS Question")
		question.update({"question": text, "type": "Choices"})
		for index, option in enumerate(options, 1):
			question.set(f"option_{index}", option)
			question.set(f"is_correct_{index}", int(index - 1 == correct))
		question.save()
		quiz.append("questions", {"question": question.name, "marks": 5})
	quiz.save()
	return quiz


def enroll(student, course):
	if not frappe.db.exists("LMS Enrollment", {"member": student.name, "course": course.name}):
		frappe.get_doc({"doctype": "LMS Enrollment", "member": student.name, "course": course.name}).insert()


def create_progress(course, student, limit):
	lessons = frappe.get_all("Course Lesson", {"course": course.name}, pluck="name", limit=limit, order_by="creation asc")
	for lesson in lessons:
		if not frappe.db.exists("LMS Course Progress", {"member": student.name, "lesson": lesson, "course": course.name}):
			frappe.get_doc({"doctype": "LMS Course Progress", "member": student.name, "lesson": lesson, "course": course.name, "status": "Complete"}).insert()
	progress = get_course_progress(course.name, student.name)
	frappe.db.set_value("LMS Enrollment", {"member": student.name, "course": course.name}, "progress", progress)
