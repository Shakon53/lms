import { call } from 'frappe-ui'

export type LMSLanguageCode = 'en' | 'ru' | 'kk'

export const LMS_LANGUAGES: ReadonlyArray<{
	code: LMSLanguageCode
	shortLabel: string
	label: string
}> = [
	{ code: 'en', shortLabel: 'EN', label: 'English' },
	{ code: 'ru', shortLabel: 'RU', label: 'Русский' },
	{ code: 'kk', shortLabel: 'KZ', label: 'Қазақша' },
]

export const currentLanguage = (): LMSLanguageCode => {
	const language = document.documentElement.lang.toLowerCase().split('-')[0]
	return LMS_LANGUAGES.some(({ code }) => code === language)
		? (language as LMSLanguageCode)
		: 'en'
}

export const languageShortLabel = (language = currentLanguage()): string =>
	LMS_LANGUAGES.find(({ code }) => code === language)?.shortLabel || 'EN'

export const changeLanguage = async (language: LMSLanguageCode): Promise<void> => {
	if (language === currentLanguage()) return
	await call('lms.lms.api.set_language', { language })
	window.location.reload()
}
