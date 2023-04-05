## Database-Study-minimal-plus
### Input
```yaml
study_set:
- abstract: abstract isn't actually required
  id: nmdc:sty-11-abc
  name: name isn't actually required
- abstract: abstract isn't actually required
  id: nmdc:sty-11-zzz
  name: name isn't actually required

```
## Database-Study-missing-id
### Input
```yaml
study_set:
- abstract: abstract isn't actually required
  name: name isn't actually required
- abstract: abstract isn't actually required
  id: nmdc:sty-11-zzz
  name: name isn't actually required

```
## Database-Study-bad-id-pattern-1
### Input
```yaml
study_set:
- abstract: abstract isn't actually required
  id: study:1
  name: name isn't actually required
- abstract: abstract isn't actually required
  id: nmdc:sty-11-zzz
  name: name isn't actually required

```
## Database-Study-bad-id-pattern-2
### Input
```yaml
study_set:
- abstract: abstract isn't actually required
  id: study:1
  name: name isn't actually required
- abstract: abstract isn't actually required
  id: nmdc:sty-11-zzz
  name: name isn't actually required

```
