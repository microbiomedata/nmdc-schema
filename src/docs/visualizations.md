# Visualizations

## Inter-collection relationship diagram

<!-- Note: `visualizations/collection-graph.html` does not exist in the source code repository.
           It gets generated as part of the documentation build process. -->

This **inter-collection relationship diagram** shows the database **collections** described by the schema, and the **relationships** between those collections.

Each circle represents a collection. Each arrow represents all of the fields that documents in one collection—the one 
at that arrow's tail—can use to refer to documents in another collection—the one at that arrow's head. If you click on a circle, the names of the fields will appear on the arrows connected to that circle.

<iframe src="collection-graph.html" width="100%" height="600" style="border:none;"></iframe>

