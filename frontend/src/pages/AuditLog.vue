<template>
	<ListPage
		:breadcrumbs="breadcrumbs"
		:title="__('Audit Log')"
		layout="list"
		:columns="columns"
		:rows="rows"
		:loading="audit.loading"
		:has-next-page="hasNextPage"
		:total-count="null"
		:list-options="{ selectable: false, showTooltip: false }"
		empty-name="Audit events"
		empty-icon="lucide-scroll-text"
		@load-more="loadMore"
	>
		<template #filters>
			<Select
				v-model="doctype"
				:options="doctypeOptions"
				:placeholder="__('Document type')"
			/>
			<FormControl
				v-model="user"
				type="text"
				:placeholder="__('User email')"
				:aria-label="__('Filter by user email')"
			/>
		</template>
		<template #cell="{ column, value }">
			<span v-if="column.key === 'creation'" class="text-sm text-ink-gray-5">
				{{ dayjs(value).format('DD MMM YYYY, HH:mm') }}
			</span>
			<span v-else-if="column.key === 'changes'" class="text-sm text-ink-gray-7">
				{{ value || __('Document metadata changed') }}
			</span>
			<span v-else>{{ value }}</span>
		</template>
	</ListPage>
</template>

<script setup>
import { computed, inject, onMounted, ref, watch } from 'vue'
import { createResource, FormControl, usePageMeta } from 'frappe-ui'
import { useRouter } from 'vue-router'
import ListPage from '@/components/Layouts/ListPage.vue'
import Select from '@/components/Controls/Select.vue'
import { usersStore } from '@/stores/user'
import { sessionStore } from '@/stores/session'

const PAGE_LENGTH = 50
const router = useRouter()
const dayjs = inject('$dayjs')
const { userResource } = usersStore()
const { brand } = sessionStore()
const doctype = ref('')
const user = ref('')
const start = ref(0)
const rows = ref([])
const hasNextPage = ref(false)

const doctypes = [
	'LMS Course',
	'Course Lesson',
	'LMS Enrollment',
	'LMS Batch',
	'LMS Batch Enrollment',
	'LMS Assignment Submission',
	'LMS Quiz Submission',
	'LMS Certificate',
	'LMS Payment',
]
const doctypeOptions = computed(() => [
	{ label: __('All document types'), value: '' },
	...doctypes.map((value) => ({ label: __(value), value })),
])

const columns = [
	{ label: __('Date'), key: 'creation', width: '180px' },
	{ label: __('User'), key: 'owner', width: '220px' },
	{ label: __('Document type'), key: 'ref_doctype', width: '190px' },
	{ label: __('Document'), key: 'docname', width: '220px' },
	{ label: __('Changes'), key: 'changes' },
]

const audit = createResource({
	url: 'lms.lms.api.get_audit_log',
	makeParams() {
		return {
			start: start.value,
			page_length: PAGE_LENGTH,
			doctype: doctype.value || null,
			user: user.value.trim() || null,
		}
	},
	onSuccess(data) {
		const next = data.map((entry) => ({
			...entry,
			changes: [
				...entry.changed_fields,
				entry.added_rows ? __('{0} rows added').format(entry.added_rows) : '',
				entry.removed_rows ? __('{0} rows removed').format(entry.removed_rows) : '',
			]
				.filter(Boolean)
				.join(', '),
		}))
		rows.value = start.value ? [...rows.value, ...next] : next
		hasNextPage.value = data.length === PAGE_LENGTH
	},
})

const reload = () => {
	start.value = 0
	rows.value = []
	audit.reload()
}
const loadMore = () => {
	start.value += PAGE_LENGTH
	audit.reload()
}

let filterTimer
watch([doctype, user], () => {
	clearTimeout(filterTimer)
	filterTimer = setTimeout(reload, 300)
})

onMounted(async () => {
	await userResource.promise
	if (!userResource.data?.is_system_manager) {
		router.replace({ name: 'Home' })
		return
	}
	audit.fetch()
})

const breadcrumbs = computed(() => [
	{ label: __('Audit Log'), route: { name: 'AuditLog' } },
])

usePageMeta(() => ({ title: __('Audit Log'), icon: brand.favicon }))
</script>
