with
    url_code := <str>$url_code,
select Meeting { url_code, start_date, end_date, title, location }
filter .url_code = url_code
limit 1