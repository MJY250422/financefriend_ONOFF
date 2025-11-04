"""
Supabase PostgreSQL 연결 테스트 스크립트
"""
import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# 환경 변수 로드
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def test_connection():
    """데이터베이스 연결 테스트"""
    print("[INFO] Testing Supabase connection...")
    
    # DATABASE_URL 확인
    if not DATABASE_URL:
        print("[ERROR] DATABASE_URL not found in .env file")
        print("[TIP] Create .env file with: DATABASE_URL=postgresql://...")
        return False
    
    # 비밀번호 마스킹해서 출력
    masked_url = DATABASE_URL
    if "@" in DATABASE_URL:
        parts = DATABASE_URL.split("@")
        if ":" in parts[0]:
            user_pass = parts[0].split("://")[1]
            user = user_pass.split(":")[0]
            masked_url = DATABASE_URL.replace(user_pass, f"{user}:***")
    
    print(f"[INFO] Database URL: {masked_url}")
    
    # PostgreSQL인지 확인
    if not DATABASE_URL.startswith("postgresql"):
        print("[WARNING] DATABASE_URL does not start with 'postgresql'")
        print(f"[WARNING] Current: {DATABASE_URL[:20]}...")
        print("[TIP] Supabase uses PostgreSQL. Check your connection string.")
    
    try:
        # 엔진 생성
        print("[INFO] Creating database engine...")
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10
        )
        
        # 연결 테스트
        print("[INFO] Testing connection...")
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"[SUCCESS] Connected to Supabase PostgreSQL!")
            print(f"[INFO] Server version: {version[:80]}...")
            
            # 스키마 확인
            print("\n[INFO] Checking existing tables...")
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """))
            tables = result.fetchall()
            
            if tables:
                print(f"[INFO] Found {len(tables)} table(s):")
                for table in tables:
                    print(f"  - {table[0]}")
            else:
                print("[INFO] No tables found. Run 'python main.py' to create tables.")
        
        print("\n[SUCCESS] Connection test passed!")
        return True
        
    except Exception as e:
        print(f"\n[ERROR] Connection failed: {e}")
        print("\n[TROUBLESHOOTING]")
        
        if "password authentication failed" in str(e):
            print("  - Check your password in DATABASE_URL")
            print("  - Special characters in password? Try URL encoding")
            print("    Example: @ → %40, # → %23")
        
        elif "could not connect to server" in str(e):
            print("  - Check your HOST in DATABASE_URL")
            print("  - Verify internet connection")
            print("  - Check if Supabase project is active")
        
        elif "No module named" in str(e):
            print("  - Install PostgreSQL driver:")
            print("    pip install psycopg2-binary")
        
        else:
            print(f"  - Error type: {type(e).__name__}")
            print(f"  - See SUPABASE_SETUP.md for troubleshooting")
        
        return False


def check_driver():
    """PostgreSQL 드라이버 확인"""
    print("\n[INFO] Checking PostgreSQL driver...")
    try:
        import psycopg2
        print(f"[SUCCESS] psycopg2 installed: version {psycopg2.__version__}")
        return True
    except ImportError:
        print("[ERROR] psycopg2 not installed")
        print("[ACTION] Run: pip install psycopg2-binary")
        return False


def main():
    """메인 함수"""
    print("=" * 60)
    print("Supabase PostgreSQL Connection Test")
    print("=" * 60)
    
    # 드라이버 확인
    if not check_driver():
        print("\n[FAILED] Please install psycopg2-binary first")
        sys.exit(1)
    
    print()
    
    # 연결 테스트
    if test_connection():
        print("\n" + "=" * 60)
        print("✅ All tests passed! You're ready to use Supabase.")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("❌ Connection test failed. See troubleshooting above.")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()

