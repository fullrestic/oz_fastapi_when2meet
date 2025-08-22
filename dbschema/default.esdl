module default {
    abstract type Auditable{
        required created_at -> cal::local_datetime{
            readonly := true;
            default := cal::to_local_datetime(datetime_current(), 'Asia/Seoul');
        }
    }

    type Meeting extending Auditable{
        required url_code: str{
            constraint exclusive;   # sql의 unique
            readonly := true
        };
        start_date -> cal::local_date;
        end_date -> cal::local_date;
        required title: str{
            default := "";
        };
        required location: str{
            default := ""
        };
        multi participants := .< meeting[is Participant];
    }

    type Participant extending Auditable{
        required name -> str;
        required meeting -> Meeting; # single link
        multi dates := .< participant[is ParticipantDate];
    }

    type ParticipantDate extending Auditable{
        required date -> cal::local_date;
        required participant -> Participant{
            on target delete delete source;
        }
        constraint exclusive on ((.date, .participant));
        required storred -> bool{
            default := false;
        }
        required enabled -> bool{
            default := true; # unabled 가 true일 때 "참가 가능한 날"
        }
    }
}
