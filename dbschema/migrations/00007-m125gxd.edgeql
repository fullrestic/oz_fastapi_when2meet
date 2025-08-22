CREATE MIGRATION m125gxd3qfaxp4tg45lverygm5ofxmcvxa2zak2wyiiperlyiwdb3a
    ONTO m1l7qih7pdldq63lm4mjiyyfzhe3czv5r3pf2im5w44g3zjjdgehjq
{
  CREATE TYPE default::Participant EXTENDING default::Auditable {
      CREATE REQUIRED LINK meeting: default::Meeting;
      CREATE REQUIRED PROPERTY name: std::str;
  };
  ALTER TYPE default::Meeting {
      CREATE MULTI LINK participants := (.<meeting[IS default::Participant]);
  };
  CREATE TYPE default::ParticipantDate EXTENDING default::Auditable {
      CREATE REQUIRED LINK participant: default::Participant {
          ON TARGET DELETE DELETE SOURCE;
      };
      CREATE REQUIRED PROPERTY date: cal::local_date;
      CREATE CONSTRAINT std::exclusive ON ((.date, .participant));
      CREATE REQUIRED PROPERTY enabled: std::bool {
          SET default := true;
      };
      CREATE REQUIRED PROPERTY storred: std::bool {
          SET default := false;
      };
  };
  ALTER TYPE default::Participant {
      CREATE MULTI LINK dates := (.<participant[IS default::ParticipantDate]);
  };
};
