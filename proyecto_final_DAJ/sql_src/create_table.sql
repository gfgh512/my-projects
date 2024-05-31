CREATE TABLE yellow_taxi_trips (
    trip_id SERIAL PRIMARY KEY,
    VendorID SMALLINT NOT NULL,
    tpep_pickup_datetime TIMESTAMP NOT NULL,
    tpep_pickup_date DATE NOT NULL,
    tpep_dropoff_datetime TIMESTAMP NOT NULL,
    Passenger_count SMALLINT NULL,
    Trip_distance NUMERIC(8,2) NOT NULL,
    PULocationID SMALLINT NOT NULL,
    DOLocationID SMALLINT NOT NULL,
    RateCodeID SMALLINT NULL,
    Store_and_fwd_flag CHAR(1) NULL,
    Payment_type SMALLINT NOT NULL,
    Fare_amount NUMERIC(8,2) NOT NULL,
    Extra NUMERIC(5,2) NOT NULL,
    MTA_tax NUMERIC(3,2) NOT NULL,
    Improvement_surcharge NUMERIC(3,2) NOT NULL,
    Tip_amount NUMERIC(6,2) NOT NULL,
    Tolls_amount NUMERIC(6,2) NOT NULL,
    Total_amount NUMERIC(8,2) NOT NULL,
    Congestion_Surcharge NUMERIC(5,2),
    Airport_fee NUMERIC(4,2)
);

CREATE INDEX idx_tpep_pickup_date ON yellow_taxi_trips (tpep_pickup_date);