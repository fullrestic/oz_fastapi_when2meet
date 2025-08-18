from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

# DB 두가지 사용
edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원해는 어떤 DB를 쓰는지 URL에 적을 필요 없음! 강의에서만 이렇게
# 실전에서는 db 이름을 url에 넣지 말 것!


@edgedb_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
