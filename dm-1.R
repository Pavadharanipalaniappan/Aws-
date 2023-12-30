calculateGear <- function(gearRatio, engineRPM, tireDiameter) {
  finalDriveRatio <- 3.42  # Replace with the actual final drive ratio of your vehicle
  
  # Calculate the speed at the wheels in miles per hour
  wheelSpeedMPH <- (engineRPM * tireDiameter * gearRatio * finalDriveRatio * 0.0113636) / 63360
  
  # Calculate the gear based on the wheel speed
  if (wheelSpeedMPH < 10) {
    gear <- "Low Gear"
  } else if (wheelSpeedMPH < 20) {
    gear <- "Second Gear"
  } else if (wheelSpeedMPH < 30) {
    gear <- "Third Gear"
  } else if (wheelSpeedMPH < 40) {
    gear <- "Fourth Gear"
  } else {
    gear <- "Fifth Gear"
  }
  
  return(gear)
}

# Example usage
gearRatio <- 2.7
engineRPM <- 3000
tireDiameter <- 26
gear <- calculateGear(gearRatio, engineRPM, tireDiameter)
print(gear)

