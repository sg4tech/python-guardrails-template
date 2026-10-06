.PHONY: verify test lint typecheck security complexity cognitive-complexity annotation-complexity architecture dependencies copy-paste dead-code coverage secret-scan dependency-audit install-hooks

test:
	docker compose run --rm test

lint:
	docker compose run --rm lint
	docker compose run --rm format-check

typecheck:
	docker compose run --rm typecheck

security:
	docker compose run --rm security

complexity:
	docker compose run --rm complexity

annotation-complexity:
	docker compose run --rm annotation-complexity

cognitive-complexity:
	docker compose run --rm cognitive-complexity

secret-scan:
	git ls-files -z | docker compose run --rm -T secret-scan

install-hooks:
	git config core.hooksPath .githooks

architecture:
	docker compose run --rm architecture

dependencies:
	docker compose run --rm dependencies

copy-paste:
	docker compose run --rm copy-paste

dead-code:
	docker compose run --rm dead-code

coverage:
	docker compose run --rm coverage

dependency-audit:
	docker compose run --rm dependency-audit

verify: lint typecheck security complexity cognitive-complexity annotation-complexity architecture dependencies copy-paste dead-code coverage secret-scan dependency-audit
