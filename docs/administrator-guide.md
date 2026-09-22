# Administrator guide

## Initial configuration

1. Set the brand name, logo, contact email, and public access policy in Settings.
2. Configure an outgoing email account and test registration, password reset,
   enrollment confirmation, and certificate delivery.
3. Create categories and assign only the roles each staff member needs.
4. Configure Zoom or Google Meet only for accounts authorized to host classes.
5. Configure payment gateways with test credentials before enabling paid enrollment.

## Routine administration

- Review failed background jobs, email delivery, storage, and backup age daily.
- Review membership and privileged roles regularly.
- Test course enrollment, submission, and certificate flows after each upgrade.
- Export or back up records before bulk imports and structural course changes.

## Change history

YU-LMS stores Frappe Version records for critical learning and financial
documents, including courses, lessons, enrollments, submissions, certificates,
and payments. Use the document timeline in Desk to review who changed a record,
when it changed, and which fields were modified. Restrict access to Version and
Activity Log records to trusted administrators.

## Incident response

If suspicious access or an incorrect privileged action is reported, preserve the
relevant logs, disable affected credentials, record the time and impacted records,
and restore service only after the cause is understood.
