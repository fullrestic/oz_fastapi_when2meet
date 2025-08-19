CREATE MIGRATION m17itvhrq7ckr43pfljbyxpmmq2pfiisw2xwzimhcuwgns4d4bgtga
    ONTO m1kpuhd7ouykj2sfv7joihk63ejlogi2asw7sl5yycb2n64z6lp5gq
{
  CREATE ABSTRACT TYPE default::Auditable {
      CREATE REQUIRED PROPERTY created_at: cal::local_datetime {
          SET default := (cal::to_local_datetime(std::datetime_current(), 'Asia/Seoul'));
          SET readonly := true;
      };
  };
  CREATE TYPE default::Meeting EXTENDING default::Auditable {
      CREATE REQUIRED PROPERTY url_code: std::str {
          SET readonly := true;
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
