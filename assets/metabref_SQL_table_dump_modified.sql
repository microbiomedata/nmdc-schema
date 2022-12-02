-- alter table ... owner to metab_user (not developer)
--create type  activity as (f1 int,
--f2 text);
--create type separation_types as (f1 int,
--f2 text);

create sequence if not exists "containerType_id_seq";

create sequence if not exists "molecularData_id_seq";

create sequence if not exists "massSpectrumObject_id_seq";

create sequence if not exists "detectionActivity_id_seq";

create sequence if not exists "deviceType_id_seq";

create sequence if not exists "metadata_object_id_seq";

create sequence if not exists "quantityValue_id_seq";

create sequence if not exists "sampleOperations_id_seq";

create sequence if not exists "separationActivity_id_seq";

create sequence if not exists "referenceMaterial_id_seq";

create sequence if not exists "user_id_seq";
-- Table: public.alembic_version
-- DROP TABLE IF EXISTS public.alembic_version;

create table if not exists public.alembic_version
(
    version_num character varying(32) collate pg_catalog."default" not null,
    constraint alembic_version_pkc primary key (version_num)
)

tablespace pg_default;

alter table if exists public.alembic_version
    owner to metab_user;
-- Table: public.containerType
-- DROP TABLE IF EXISTS public."containerType";

create table if not exists public."containerType"
(
    id integer not null default nextval('"containerType_id_seq"'::regclass),
    description character varying collate pg_catalog."default",
    type character varying collate pg_catalog."default",
    size character varying collate pg_catalog."default",
    was_generated_by character varying collate pg_catalog."default",
    constraint "containerType_pkey" primary key (id)
)

tablespace pg_default;

alter table if exists public."containerType"
    owner to metab_user;
-- Table: public.molecularData
-- DROP TABLE IF EXISTS public."molecularData";

create table if not exists public."molecularData"
(
    id integer not null default nextval('"molecularData_id_seq"'::regclass),
    inchikey character varying collate pg_catalog."default" not null,
    name character varying collate pg_catalog."default" not null,
    formula character varying collate pg_catalog."default",
    casno character varying collate pg_catalog."default",
    inchi character varying collate pg_catalog."default" not null,
    chebi character varying collate pg_catalog."default",
    smiles character varying collate pg_catalog."default",
    kegg character varying collate pg_catalog."default",
    iupac_name character varying collate pg_catalog."default",
    traditional_name character varying collate pg_catalog."default",
    common_name character varying collate pg_catalog."default",
    match_name character varying collate pg_catalog."default",
    derivativenum character varying collate pg_catalog."default",
    constraint "molecularData_pkey" primary key (id)
)

tablespace pg_default;

alter table if exists public."deviceType"
    owner to metab_user;
-- Table: public.massSpectrumObject
-- DROP TABLE IF EXISTS public."massSpectrumObject";

create table if not exists public."massSpectrumObject"
(
    id integer not null default nextval('"massSpectrumObject_id_seq"'::regclass),
    molecular_data_id integer,
    type character varying collate pg_catalog."default",
    source character varying collate pg_catalog."default",
    version character varying collate pg_catalog."default",
    collision_energy character varying collate pg_catalog."default",
    precursor_ion double precision,
    peak_count integer not null,
    rt double precision not null,
    mz bytea not null,
    abundance bytea not null,
    polarity character varying collate pg_catalog."default",
    constraint "massSpectrumObject_pkey" primary key (id),
    constraint "massSpectrumObject_molecular_data_id_fkey" foreign key (molecular_data_id)
        references public."molecularData" (id) match simple
        on
update
	no action
        on
	delete
		no action
)

tablespace pg_default;

alter table if exists public."massSpectrumObject"
    owner to metab_user;
-- Table: public.detectionActivity
-- DROP TABLE IF EXISTS public."detectionActivity";

create table if not exists public."detectionActivity"
(
    id integer not null default nextval('"detectionActivity_id_seq"'::regclass),
    spectrum_id integer,
    type character varying collate pg_catalog."default",
    analyzer character varying collate pg_catalog."default",
    acquisition character varying collate pg_catalog."default",
    ionization character varying collate pg_catalog."default",
    rawdata_url character varying collate pg_catalog."default",
    constraint "detectionActivity_pkey" primary key (id),
    constraint "detectionActivity_spectrum_id_fkey" foreign key (spectrum_id)
        references public."massSpectrumObject" (id) match simple
        on
update
	no action
        on
	delete
		no action
)

tablespace pg_default;

alter table if exists public."detectionActivity"
    owner to metab_user;
-- Table: public.deviceType
-- DROP TABLE IF EXISTS public."deviceType";

create table if not exists public."deviceType"
(
    id integer not null default nextval('"deviceType_id_seq"'::regclass),
    description character varying collate pg_catalog."default",
    type character varying collate pg_catalog."default",
    was_generated_by character varying collate pg_catalog."default",
    constraint "deviceType_pkey" primary key (id)
)

tablespace pg_default;

alter table if exists public."deviceType"
    owner to metab_user;
-- Table: public.metadata_object
-- DROP TABLE IF EXISTS public.metadata_object;

create table if not exists public.metadata_object
(
    id integer not null default nextval('metadata_object_id_seq'::regclass),
    molecular_data_id integer,
    source character varying collate pg_catalog."default",
    source_temp_c double precision,
    ev double precision,
    classify character varying collate pg_catalog."default",
    comment character varying collate pg_catalog."default",
    constraint metadata_object_pkey primary key (id),
    constraint metadata_object_molecular_data_id_fkey foreign key (molecular_data_id)
        references public."molecularData" (id) match simple
        on
update
	no action
        on
	delete
		no action
)

tablespace pg_default;

alter table if exists public.metadata_object
    owner to metab_user;
-- Table: public.quantityValue
-- DROP TABLE IF EXISTS public."quantityValue";

create table if not exists public."quantityValue"
(
    id integer not null default nextval('"quantityValue_id_seq"'::regclass),
    description character varying collate pg_catalog."default",
    has_numeric_value numeric,
    has_minimum_numeric_value numeric,
    has_maximum_numeric_value numeric,
    has_raw_value character varying collate pg_catalog."default",
    type character varying collate pg_catalog."default",
    has_unit character varying collate pg_catalog."default",
    was_generated_by character varying collate pg_catalog."default",
    constraint "quantityValue_pkey" primary key (id)
)

tablespace pg_default;

alter table if exists public."quantityValue"
    owner to metab_user;
-- Table: public.separationActivity
-- DROP TABLE IF EXISTS public."separationActivity";

create table if not exists public."separationActivity"
(
    id integer not null default nextval('"separationActivity_id_seq"'::regclass),
    type separation_types not null,
    detection_id integer,
    "column" character varying collate pg_catalog."default",
    mobile_phase character varying collate pg_catalog."default",
    gradient character varying collate pg_catalog."default",
    flow_rate character varying collate pg_catalog."default",
    instrument_name character varying collate pg_catalog."default",
    column_temp integer,
    sample_chamber_temp integer,
    separation_id integer,
    column_lc character varying collate pg_catalog."default",
    filter character varying collate pg_catalog."default",
    water_acquity character varying collate pg_catalog."default",
    column_temp_lc character varying collate pg_catalog."default",
    gradient_lc character varying collate pg_catalog."default",
    acceleration character varying collate pg_catalog."default",
    seal_wash character varying collate pg_catalog."default",
    max_pressure character varying collate pg_catalog."default",
    separation_id_gc integer,
    derivative integer,
    constraint "separationActivity_pkey" primary key (id),
    constraint "separationActivity_detection_id_fkey" foreign key (detection_id)
        references public."detectionActivity" (id) match simple
        on
update
	no action
        on
	delete
		no action,
		constraint "separationActivity_separation_id_fkey" foreign key (separation_id)
        references public."separationActivity" (id) match simple
        on
		update
			no action
        on
			delete
				no action,
				constraint "separationActivity_separation_id_gc_fkey" foreign key (separation_id_gc)
        references public."separationActivity" (id) match simple
        on
				update
					no action
        on
					delete
						no action
)

tablespace pg_default;

alter table if exists public."separationActivity"
    owner to metab_user;
-- Table: public.sampleOperations
-- DROP TABLE IF EXISTS public."sampleOperations";

create table if not exists public."sampleOperations"
(
    id integer not null default nextval('"sampleOperations_id_seq"'::regclass),
    detection_id integer,
    separation_id integer,
    type activity not null,
    material_input integer,
    derivatization character varying collate pg_catalog."default",
    material_output character varying collate pg_catalog."default",
    reaction_aided_by character varying collate pg_catalog."default",
    reaction_temperature double precision,
    reaction_time double precision,
    extractant character varying collate pg_catalog."default",
    sample_volume double precision,
    mixing character varying collate pg_catalog."default",
    speed character varying collate pg_catalog."default",
    analyte_id integer not null,
    source_mat_id integer,
    container_type character varying collate pg_catalog."default",
    volume_unit character varying collate pg_catalog."default",
    duration double precision,
    unit character varying collate pg_catalog."default",
    volume integer,
    concentration character varying collate pg_catalog."default",
    starting_amount double precision,
    material_component_separation character varying collate pg_catalog."default",
    value double precision,
    analyte_volume integer,
    acid character varying collate pg_catalog."default",
    "pH" double precision,
    celsius_temperature double precision,
    separation_method character varying collate pg_catalog."default",
    filter character varying collate pg_catalog."default",
    material_pore_size double precision,
    conditioning character varying collate pg_catalog."default",
    conditioning_volume integer,
    constraint "sampleOperations_pkey" primary key (id),
    constraint "sampleOperations_detection_id_fkey" foreign key (detection_id)
        references public."detectionActivity" (id) match simple
        on
update
	no action
        on
	delete
		no action,
		constraint "sampleOperations_separation_id_fkey" foreign key (separation_id)
        references public."separationActivity" (id) match simple
        on
		update
			no action
        on
			delete
				no action
)

tablespace pg_default;

alter table if exists public."sampleOperations"
    owner to metab_user;
-- Table: public.referenceMaterial
-- DROP TABLE IF EXISTS public."referenceMaterial";

create table if not exists public."referenceMaterial"
(
    id integer not null default nextval('"referenceMaterial_id_seq"'::regclass),
    sample_operation_id integer,
    type character varying collate pg_catalog."default",
    source character varying collate pg_catalog."default",
    constraint "referenceMaterial_pkey" primary key (id),
    constraint "referenceMaterial_sample_operation_id_fkey" foreign key (sample_operation_id)
        references public."sampleOperations" (id) match simple
        on
update
	no action
        on
	delete
		no action
)

tablespace pg_default;

alter table if exists public."referenceMaterial"
    owner to metab_user;
-- Table: public.user
-- DROP TABLE IF EXISTS public."user";

create table if not exists public."user"
(
    id integer not null default nextval('user_id_seq'::regclass),
    email character varying(100) collate pg_catalog."default",
    password character varying collate pg_catalog."default",
    username character varying(100) collate pg_catalog."default",
    api_key character varying collate pg_catalog."default",
    first_name character varying(100) collate pg_catalog."default",
    last_name character varying(100) collate pg_catalog."default",
    constraint user_pkey primary key (id)
)

tablespace pg_default;

alter table if exists public."user"
    owner to metab_user;