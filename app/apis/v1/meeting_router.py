from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.services.meeting_service_edgedb import (
    service_create_meeting_edgedb,
    service_get_meeting_edgedb,
)
from app.services.meeting_service_mysql import service_create_meeting_mysql

# DB 두가지 사용
edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원해는 어떤 DB를 쓰는지 URL에 적을 필요 없음! 강의에서만 이렇게
# 실전에서는 db 이름을 url에 넣지 말 것!


@edgedb_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_edgedb()).url_code)


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)


@edgedb_router.get(
    "/{meeting_url_code}",  # path variable - api 경로로부터 변수를 받아들임
    description="meeting을 조회합니다.",
)
async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeetingResponse:  # path variable type 정의
    meeting = await service_get_meeting_edgedb(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"meeting with url_code: {meeting_url_code} not found",
        )
    return GetMeetingResponse(url_code=meeting_url_code)


@mysql_router.get(
    "/{meeting_url_code}",  # path variable - api 경로로부터 변수를 받아들임
    description="meeting을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:  # path variable type 정의
    return GetMeetingResponse(url_code=meeting_url_code)
