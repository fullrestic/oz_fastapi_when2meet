CREATE MIGRATION m1l7qih7pdldq63lm4mjiyyfzhe3czv5r3pf2im5w44g3zjjdgehjq
    ONTO m17itvhrq7ckr43pfljbyxpmmq2pfiisw2xwzimhcuwgns4d4bgtga
{
  ALTER TYPE default::Meeting {
      CREATE PROPERTY end_date: cal::local_date;
      CREATE REQUIRED PROPERTY location: std::str {
          SET default := '';
      };
      CREATE PROPERTY start_date: cal::local_date;
      CREATE REQUIRED PROPERTY title: std::str {
          SET default := '';
      };
  };
};
