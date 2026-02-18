

SELECT
    CAST(temperature AS FLOAT) AS temp_celsius,
    CAST(windspeed AS FLOAT) AS wind_speed_kmh,
    CAST(weathercode AS INTEGER) AS weather_condition_code,
    CAST(ingested_at AS TIMESTAMP) AS record_timestamp
FROM "airflow"."public"."bronze_weather"
WHERE temperature IS NOT NULL