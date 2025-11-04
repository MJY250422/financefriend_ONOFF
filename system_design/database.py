"""
데이터베이스 설정 및 세션 관리
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from db_schema_design import Base
import os
import sys

# 데이터베이스 URL 설정
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./financefriend.db"  # 기본값을 SQLite로 변경 (개발용)
)

# SQLite와 PostgreSQL에 따라 connect_args 설정
connect_args = {}
engine_kwargs = {
    "echo": True,
    "pool_pre_ping": True,
}

if DATABASE_URL.startswith("postgresql"):
    # PostgreSQL 사용 시 (선택사항)
    # psycopg2가 설치되어 있어야 함
    try:
        import psycopg2
        connect_args = {"client_encoding": "utf8"}
    except ImportError:
        print("⚠️ WARNING: psycopg2 not installed. PostgreSQL will not work.")
        print("   For SQLite, this is OK. For PostgreSQL, run: pip install psycopg2-binary")
elif DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}  # SQLite 멀티스레드 지원

engine_kwargs["connect_args"] = connect_args

# 엔진 생성
try:
    engine = create_engine(DATABASE_URL, **engine_kwargs)
except Exception as e:
    print(f"❌ Database engine creation error: {e}")
    print(f"   DATABASE_URL: {DATABASE_URL}")
    if DATABASE_URL.startswith("postgresql"):
        print("   Tip: Install PostgreSQL driver with: pip install psycopg2-binary")
        print("   Or use SQLite instead: DATABASE_URL=sqlite:///./financefriend.db")
    sys.exit(1)

# 세션 팩토리 생성
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def init_db():
    """데이터베이스 테이블 생성"""
    try:
        Base.metadata.create_all(bind=engine)
        print("[OK] Database tables created successfully")
    except Exception as e:
        print(f"[ERROR] Database initialization error: {e}")
        raise


def get_db() -> Session:
    """
    데이터베이스 세션 의존성
    FastAPI 엔드포인트에서 사용
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()