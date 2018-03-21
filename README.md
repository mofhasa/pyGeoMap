# pyGeoMap

Interface for plotting geographical maps and exporting them in different formats like pdf, docx, etc.

**Initialization**
- upperRightCorner: (latitude, longitude) tuple for the upper right corner of the map.
- lowerLeftCorner: (latitude, longitude) tuple for the lower left corner of the map.
- center: (latitude, longitude) tuple for center of the map.
- shapefiles: draw country/legislative borders for the desired country/area/continent. (default is None)
- pins: markers on the map (default is None)

**plot**

Plots markers with the provided pins.

**clear**

Clears all the markers.

**saveToPdf**

Saves the map to a pdf

---

#### Future Work
- Export to other formats like jpeg, docx, etc
- Choices for styles of the map and markers