package mockstubexample;

import java.io.IOException;

public class FlightException extends IOException {
    public FlightException(String message) {
        super(message);
    }
}

