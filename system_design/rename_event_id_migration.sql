-- ========================================
-- event_logs 테이블의 id 컬럼을 event_id로 변경
-- ========================================
-- 실행 날짜: 2025-11-06
-- 목적: 컬럼명 명확화 (id -> event_id)

-- 1. 기존 컬럼명 변경
ALTER TABLE event_logs 
RENAME COLUMN id TO event_id;

-- 2. 코멘트 업데이트
COMMENT ON COLUMN event_logs.event_id IS '이벤트 로그 고유 ID';

-- 3. 시퀀스 이름도 변경 (선택사항)
-- PostgreSQL이 자동으로 생성한 시퀀스명을 변경
ALTER SEQUENCE IF EXISTS event_logs_id_seq RENAME TO event_logs_event_id_seq;

-- 4. 변경 확인 쿼리
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'event_logs'
ORDER BY ordinal_position;

-- 완료! ✅

