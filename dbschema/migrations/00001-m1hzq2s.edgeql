CREATE MIGRATION m1hzq2sbc32slhoml2p37z7am2odvnwvr7stf2pahyk3bi76wlkeoq
    ONTO initial
{
  CREATE TYPE default::Person {
      CREATE REQUIRED PROPERTY name: std::str;
  };
  CREATE TYPE default::Movie {
      CREATE MULTI LINK actors: default::Person;
      CREATE PROPERTY tilte: std::str;
  };
};
