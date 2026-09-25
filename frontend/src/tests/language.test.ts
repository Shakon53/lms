import { beforeEach, describe, expect, it, vi } from 'vitest'

const { call } = vi.hoisted(() => ({ call: vi.fn() }))
vi.mock('frappe-ui', () => ({ call }))

import {
	changeLanguage,
	currentLanguage,
	languageShortLabel,
	LMS_LANGUAGES,
} from '@/utils/language'

describe('language switching', () => {
	beforeEach(() => {
		document.documentElement.lang = 'en'
		call.mockReset()
	})

	it('offers exactly English, Russian and Kazakh', () => {
		expect(LMS_LANGUAGES.map(({ code, shortLabel }) => [code, shortLabel])).toEqual(
			[
				['en', 'EN'],
				['ru', 'RU'],
				['kk', 'KZ'],
			]
		)
	})

	it('normalises regional document languages', () => {
		document.documentElement.lang = 'ru-RU'
		expect(currentLanguage()).toBe('ru')
		expect(languageShortLabel()).toBe('RU')
	})

	it('does not call the server for the already active language', async () => {
		await changeLanguage('en')
		expect(call).not.toHaveBeenCalled()
	})

	it('sends the selected language to the LMS endpoint', async () => {
		const error = new Error('request stopped before reload')
		call.mockRejectedValueOnce(error)

		await expect(changeLanguage('kk')).rejects.toBe(error)
		expect(call).toHaveBeenCalledWith('lms.lms.api.set_language', {
			language: 'kk',
		})
	})
})
