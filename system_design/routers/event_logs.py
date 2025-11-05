"""
이벤트 로그 관리 API 라우터
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from database import get_db
from db_schema_design import EventLog
from schemas import EventLogCreate, EventLogResponse

router = APIRouter()


@router.post("/", response_model=EventLogResponse, status_code=201)
def create_event_log(event_log: EventLogCreate, db: Session = Depends(get_db)):
    """
    이벤트 로그 생성
    
    - **event_time**: 이벤트 발생 시간
    - **event_name**: 이벤트 이름 (필수)
    - **session_id**: 관련 세션 ID (선택)
    - **dialogue_id**: 관련 대화 ID (선택)
    - **surface**: 이벤트 발생 화면/위치 (선택)
    - **source**: 이벤트 소스 (선택)
    - **ref_id**: 참조 ID (선택)
    - **payload**: 추가 데이터 (JSON, 선택)
    """
    db_event_log = EventLog(**event_log.model_dump())
    db.add(db_event_log)
    db.commit()
    db.refresh(db_event_log)
    return db_event_log


@router.get("/", response_model=List[EventLogResponse])
def get_event_logs(
    skip: int = 0,
    limit: int = 100,
    session_id: Optional[int] = None,
    event_name: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    이벤트 로그 목록 조회
    
    - **skip**: 건너뛸 레코드 수
    - **limit**: 최대 반환 레코드 수 (최대 100)
    - **session_id**: 세션 ID로 필터링 (선택)
    - **event_name**: 이벤트 이름으로 필터링 (선택)
    """
    query = db.query(EventLog)
    
    if session_id:
        query = query.filter(EventLog.session_id == session_id)
    
    if event_name:
        query = query.filter(EventLog.event_name == event_name)
    
    event_logs = query.order_by(EventLog.event_time.desc()).offset(skip).limit(limit).all()
    return event_logs


@router.get("/{event_log_id}", response_model=EventLogResponse)
def get_event_log(event_log_id: int, db: Session = Depends(get_db)):
    """
    특정 이벤트 로그 조회
    
    - **event_log_id**: 이벤트 로그 ID
    """
    event_log = db.query(EventLog).filter(EventLog.id == event_log_id).first()
    if not event_log:
        raise HTTPException(status_code=404, detail="Event log not found")
    return event_log


@router.get("/session/{session_id}/events", response_model=List[EventLogResponse])
def get_session_event_logs(
    session_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    특정 세션의 이벤트 로그 조회
    
    - **session_id**: 세션 ID
    - **skip**: 건너뛸 레코드 수
    - **limit**: 최대 반환 레코드 수
    """
    event_logs = (
        db.query(EventLog)
        .filter(EventLog.session_id == session_id)
        .order_by(EventLog.event_time.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return event_logs


@router.get("/dialogue/{dialogue_id}/events", response_model=List[EventLogResponse])
def get_dialogue_event_logs(
    dialogue_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    특정 대화의 이벤트 로그 조회
    
    - **dialogue_id**: 대화 ID
    - **skip**: 건너뛸 레코드 수
    - **limit**: 최대 반환 레코드 수
    """
    event_logs = (
        db.query(EventLog)
        .filter(EventLog.dialogue_id == dialogue_id)
        .order_by(EventLog.event_time.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return event_logs


@router.delete("/{event_log_id}", status_code=204)
def delete_event_log(event_log_id: int, db: Session = Depends(get_db)):
    """
    이벤트 로그 삭제
    
    - **event_log_id**: 이벤트 로그 ID
    """
    event_log = db.query(EventLog).filter(EventLog.id == event_log_id).first()
    if not event_log:
        raise HTTPException(status_code=404, detail="Event log not found")
    
    db.delete(event_log)
    db.commit()
    return None

