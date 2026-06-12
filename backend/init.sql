INSERT INTO users (username, password_hash)
VALUES (
    'admin',
    '$2b$12$Z9lKJ4A0QmF8sE3I6t1N0.9lE0g7tBQw8M4Q6mMdXc4K5p4lI7vS2'
);

CREATE TABLE refresh_tokens (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id),
    token_hash TEXT NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    revoked BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE audit_logs (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT,
    action VARCHAR(100),
    entity_type VARCHAR(100),
    entity_id BIGINT,
    created_at TIMESTAMP DEFAULT NOW()
);