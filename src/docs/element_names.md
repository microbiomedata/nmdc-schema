Creating, managing and mentioning names in information systems is hard and consequential.

It's consequential because other people will be using the names. For example, in an nmdc-schema example data file,
the only content besides the data values are slot names form teh schema. 
The names say what values classes bear and how they are related to other classes, 
either by inlining or by mentioning instance `id`s.
In that situation, we want the names to be evocative of the points we're trying to make. If we want instances of a Person class
to say where the person lives on earth, `address` or `geo_cordinates` would probably be better slots names that
`slot_1` or `where_to_find`

It's also consequential because when we define a slot, we are essentially reserving a slot name with one particular meaning.
If we did use `where_to_find` as the name of a slot that would take values like 

```yaml
where_to_find:
    street: 123 Main Street
    town: Anytown
    state: New Carolina
```

then we will lock other people out from using it to describe where a protein is found in a cell

```yaml
where_to_find: nucleus
```

Some might argue that Protein and Person could have different `slot_usage`s for `where_to_find`, 
but `slot_usage`s should slightly customize a general slot range at the global scope into slightly more specific slot ranges.
It's not meant to allow different classes to use a slot with totally unrelated ranges.

So now the Protein/CellularLocation modeller has to pick some different name because 
