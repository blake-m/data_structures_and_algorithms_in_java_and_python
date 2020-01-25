package mockstubexample;

import java.time.LocalDate;
import java.util.List;

interface Airline {
    List<Flight> findFlight(String departureAirport,
                            String destinationAirport,
                            LocalDate flightDate) throws FlightException;
}