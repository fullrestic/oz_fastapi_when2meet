with
    participnat_id := <uuid>$participant_id,
    dates := <array<cal::local_date>>$dates
for date in array_unpack(dates) union(
    insert ParticipantDate{
        participant := <Participant>participnat_id,
        date := date,
    }
)