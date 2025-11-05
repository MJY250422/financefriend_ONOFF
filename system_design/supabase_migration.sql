-- Supabase 데이터베이스 스키마 업데이트 (2025.11.05)
-- 실행 방법: Supabase Dashboard > SQL Editor에서 실행

-- 1. News 테이블에 summary 컬럼 추가
ALTER TABLE news ADD COLUMN IF NOT EXISTS summary TEXT;

COMMENT ON COLUMN news.summary IS '뉴스 요약 (AI 생성 또는 수동 입력)';

-- 2. Event Logs 테이블 생성
CREATE TABLE IF NOT EXISTS event_logs (
    id           BIGSERIAL PRIMARY KEY,
    event_time   TIMESTAMPTZ NOT NULL,
    session_id   INTEGER REFERENCES sessions(session_id),
    dialogue_id  BIGINT REFERENCES dialogues(dialogue_id),
    event_name   TEXT NOT NULL,
    surface      TEXT,
    source       TEXT,
    ref_id       TEXT,
    payload      JSONB,
    created_at   TIMESTAMPTZ DEFAULT NOW()
);

-- 인덱스 생성 (성능 최적화)
CREATE INDEX IF NOT EXISTS idx_event_logs_event_time ON event_logs(event_time DESC);
CREATE INDEX IF NOT EXISTS idx_event_logs_session_id ON event_logs(session_id);
CREATE INDEX IF NOT EXISTS idx_event_logs_dialogue_id ON event_logs(dialogue_id);
CREATE INDEX IF NOT EXISTS idx_event_logs_event_name ON event_logs(event_name);

-- 코멘트 추가
COMMENT ON TABLE event_logs IS '사용자 이벤트 로그 테이블';
COMMENT ON COLUMN event_logs.id IS '이벤트 로그 고유 ID';
COMMENT ON COLUMN event_logs.event_time IS '이벤트 발생 시간';
COMMENT ON COLUMN event_logs.session_id IS '관련 세션 ID';
COMMENT ON COLUMN event_logs.dialogue_id IS '관련 대화 ID';
COMMENT ON COLUMN event_logs.event_name IS '이벤트 이름 (예: page_view, button_click 등)';
COMMENT ON COLUMN event_logs.surface IS '이벤트 발생 화면/위치';
COMMENT ON COLUMN event_logs.source IS '이벤트 소스';
COMMENT ON COLUMN event_logs.ref_id IS '참조 ID (뉴스 ID, 버튼 ID 등)';
COMMENT ON COLUMN event_logs.payload IS '추가 이벤트 데이터 (JSON)';
COMMENT ON COLUMN event_logs.created_at IS '레코드 생성 시간';

-- 샘플 데이터 삽입 (선택사항)
-- 기존 세션이 있다면 샘플 이벤트 로그 생성
INSERT INTO event_logs (event_time, session_id, event_name, surface, source, payload)
SELECT 
    NOW(),
    session_id,
    'session_started',
    'web',
    'browser',
    '{"user_agent": "Mozilla/5.0", "platform": "desktop"}'::jsonb
FROM sessions
WHERE session_id IN (SELECT session_id FROM sessions LIMIT 3)
ON CONFLICT DO NOTHING;

-- 마이그레이션 완료 확인
SELECT 
    'Migration completed successfully!' as status,
    (SELECT COUNT(*) FROM event_logs) as event_logs_count,
    (SELECT COUNT(*) FROM news WHERE summary IS NOT NULL) as news_with_summary_count;

