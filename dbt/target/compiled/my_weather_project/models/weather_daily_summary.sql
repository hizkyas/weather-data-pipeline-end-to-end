SELECT
    date_trunc('hour', record_timestamp) as forecast_time,
    count(*) as records_count,
    ROUND(AVG(temp_celsius)::numeric, 2) as avg_temp,
    MAX(temp_celsius) as max_temp,
    MIN(temp_celsius) as min_temp,
    ROUND(AVG(wind_speed_kmh)::numeric, 2) as avg_wind_speed
FROM "airflow"."public_silver"."stg_weather"
GROUP BY 1
ORDER BY 1 DESC