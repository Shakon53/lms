# Production operations

## Deploy an update

1. Confirm the repository and production site are backed up.
2. Fetch the intended commit and review the commit hash before deployment.
3. Build frontend assets.
4. Run database migrations for the production site.
5. Restart the application services.
6. Verify `/api/method/ping`, `/lms`, sign-in, and one authenticated learning flow.

Never deploy an uncommitted working tree or copy `.env`, private keys, database
files, or site secrets into the repository.

## Backup and restore

The systemd timer in `docker/systemd/lms-backup.timer` creates scheduled backups.
Configure `BACKUP_REMOTE` for off-site copies. A backup is considered usable only
after a restore has been tested on a separate site.

## Monitoring

The health timer checks the API and LMS page. Configure `HEALTHCHECK_PING_URL` so
an external service alerts when heartbeats stop. Also monitor disk space, queue
workers, scheduler activity, database health, TLS expiry, and outbound email.

## Rollback

Application rollback and data rollback are different operations. Do not run an
older application against a migrated database unless that version is known to be
schema-compatible. For a destructive migration, restore the matching database and
files backup together with the matching application revision.
