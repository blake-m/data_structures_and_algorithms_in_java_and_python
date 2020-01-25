package mockstubexample;

import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FlightScannerTestStubs {
    private Airline stub1 = (departureAirport, destinationAirport, flightDate) ->
            Collections.singletonList(
              new Flight("QW9999", new BigDecimal(100), "WRO", "BCN")
            );

    private Airline stub2 = (departureAirport, destinationAirport, flightDate) ->
            Collections.singletonList(
                    new Flight("QW8888", new BigDecimal(1000), "WRO", "BCN")
            );

    private Airline stub3 = (departureAirport, destinationAirport, flightDate) -> {
        throw new FlightException("Whoa! What happened!?");
    };

    @Test
    void shouldFindLowestPrice() {
        FlightScanner flightScanner = new FlightScanner(stub1, stub2, stub3);
        assertEquals("QW9999", flightScanner.findCheapestFlight(
                "some_departure", "some_destination", null)
                .getFlightNumber()
        );
    }
}