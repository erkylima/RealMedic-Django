PGDMP                 
        x            realconsulta %   10.15 (Ubuntu 10.15-0ubuntu0.18.04.1) #   12.5 (Ubuntu 12.5-0ubuntu0.20.04.1) k   H           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            I           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            J           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            K           1262    27025    realconsulta    DATABASE     v   CREATE DATABASE realconsulta WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';
    DROP DATABASE realconsulta;
                postgres    false            �            1259    27057 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public            postgres    false            �            1259    27055    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    203            L           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    202            �            1259    27067    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public            postgres    false            �            1259    27065    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    205            M           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    204            �            1259    27049    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public            postgres    false            �            1259    27047    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    201            N           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    200            �            1259    27075 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public            postgres    false            �            1259    27085    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public            postgres    false            �            1259    27083    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    209            O           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    208            �            1259    27073    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    207            P           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    206            �            1259    27093    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public            postgres    false            �            1259    27091 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    211            Q           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    210            �            1259    27184    authtoken_token    TABLE     �   CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);
 #   DROP TABLE public.authtoken_token;
       public            postgres    false            �            1259    27204    core_areaatendimento    TABLE     u   CREATE TABLE public.core_areaatendimento (
    id integer NOT NULL,
    descricao character varying(255) NOT NULL
);
 (   DROP TABLE public.core_areaatendimento;
       public            postgres    false            �            1259    27202    core_areaatendimento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_areaatendimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.core_areaatendimento_id_seq;
       public          postgres    false    216            R           0    0    core_areaatendimento_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.core_areaatendimento_id_seq OWNED BY public.core_areaatendimento.id;
          public          postgres    false    215                       1259    27490    core_atendente    TABLE     �  CREATE TABLE public.core_atendente (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(255) NOT NULL,
    usuario character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    senha character varying(255) NOT NULL,
    ativo boolean NOT NULL,
    departamento_id integer,
    perfil_id integer NOT NULL,
    user_id integer NOT NULL
);
 "   DROP TABLE public.core_atendente;
       public            postgres    false                       1259    27488    core_atendente_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_atendente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.core_atendente_id_seq;
       public          postgres    false    260            S           0    0    core_atendente_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.core_atendente_id_seq OWNED BY public.core_atendente.id;
          public          postgres    false    259            �            1259    27212    core_atendimento    TABLE     R  CREATE TABLE public.core_atendimento (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    retorno boolean NOT NULL,
    valor numeric(5,2) NOT NULL,
    tempo time without time zone NOT NULL,
    inicio_atendimento time without time zone,
    fim_atendimento time without time zone,
    pago boolean NOT NULL,
    crm_soliciante character varying(7) NOT NULL,
    "departamentoProfissional_id" integer NOT NULL,
    intervalo_id integer,
    paciente_id integer NOT NULL,
    "tipoAtendimento_id" integer NOT NULL
);
 $   DROP TABLE public.core_atendimento;
       public            postgres    false            �            1259    27210    core_atendimento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_atendimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.core_atendimento_id_seq;
       public          postgres    false    218            T           0    0    core_atendimento_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.core_atendimento_id_seq OWNED BY public.core_atendimento.id;
          public          postgres    false    217            �            1259    27220    core_atendimentosdepartamento    TABLE     �  CREATE TABLE public.core_atendimentosdepartamento (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(255),
    tipo_profissional integer NOT NULL,
    tempo_padrao time without time zone NOT NULL,
    valor_padrao numeric(5,2) NOT NULL,
    publico boolean NOT NULL,
    departamento_id integer NOT NULL,
    tipo_atendimento_id integer NOT NULL
);
 1   DROP TABLE public.core_atendimentosdepartamento;
       public            postgres    false            �            1259    27218 $   core_atendimentosdepartamento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_atendimentosdepartamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.core_atendimentosdepartamento_id_seq;
       public          postgres    false    220            U           0    0 $   core_atendimentosdepartamento_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.core_atendimentosdepartamento_id_seq OWNED BY public.core_atendimentosdepartamento.id;
          public          postgres    false    219                       1259    27428    core_cliente    TABLE     �  CREATE TABLE public.core_cliente (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(255) NOT NULL,
    usuario character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    senha character varying(255) NOT NULL,
    ativo boolean NOT NULL,
    cliente_app character varying(255) NOT NULL,
    perfil_id integer NOT NULL,
    user_id integer NOT NULL
);
     DROP TABLE public.core_cliente;
       public            postgres    false                       1259    27426    core_cliente_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.core_cliente_id_seq;
       public          postgres    false    258            V           0    0    core_cliente_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.core_cliente_id_seq OWNED BY public.core_cliente.id;
          public          postgres    false    257            �            1259    27228    core_convenio    TABLE       CREATE TABLE public.core_convenio (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(100) NOT NULL,
    descricao character varying(255) NOT NULL,
    desconto integer NOT NULL
);
 !   DROP TABLE public.core_convenio;
       public            postgres    false            �            1259    27226    core_convenio_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_convenio_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.core_convenio_id_seq;
       public          postgres    false    222            W           0    0    core_convenio_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.core_convenio_id_seq OWNED BY public.core_convenio.id;
          public          postgres    false    221            �            1259    27236    core_departamento    TABLE     0  CREATE TABLE public.core_departamento (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(255) NOT NULL,
    descricao character varying(255) NOT NULL,
    empresa_id integer,
    endereco_id integer
);
 %   DROP TABLE public.core_departamento;
       public            postgres    false            �            1259    27234    core_departamento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_departamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.core_departamento_id_seq;
       public          postgres    false    224            X           0    0    core_departamento_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.core_departamento_id_seq OWNED BY public.core_departamento.id;
          public          postgres    false    223            �            1259    27247    core_departamentoprofissional    TABLE     �   CREATE TABLE public.core_departamentoprofissional (
    id integer NOT NULL,
    departamento_id integer NOT NULL,
    profissional_id integer NOT NULL,
    tipo_profissional_id integer NOT NULL
);
 1   DROP TABLE public.core_departamentoprofissional;
       public            postgres    false            �            1259    27245 $   core_departamentoprofissional_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_departamentoprofissional_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.core_departamentoprofissional_id_seq;
       public          postgres    false    226            Y           0    0 $   core_departamentoprofissional_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.core_departamentoprofissional_id_seq OWNED BY public.core_departamentoprofissional.id;
          public          postgres    false    225            �            1259    27255    core_empresa    TABLE       CREATE TABLE public.core_empresa (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome_razao_social character varying(255) NOT NULL,
    documento character varying(18) NOT NULL
);
     DROP TABLE public.core_empresa;
       public            postgres    false            �            1259    27265    core_empresa_convenios    TABLE     �   CREATE TABLE public.core_empresa_convenios (
    id integer NOT NULL,
    empresa_id integer NOT NULL,
    convenio_id integer NOT NULL
);
 *   DROP TABLE public.core_empresa_convenios;
       public            postgres    false            �            1259    27263    core_empresa_convenios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_empresa_convenios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.core_empresa_convenios_id_seq;
       public          postgres    false    230            Z           0    0    core_empresa_convenios_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.core_empresa_convenios_id_seq OWNED BY public.core_empresa_convenios.id;
          public          postgres    false    229            �            1259    27253    core_empresa_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_empresa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.core_empresa_id_seq;
       public          postgres    false    228            [           0    0    core_empresa_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.core_empresa_id_seq OWNED BY public.core_empresa.id;
          public          postgres    false    227            �            1259    27273    core_endereco    TABLE       CREATE TABLE public.core_endereco (
    id integer NOT NULL,
    rua character varying(255) NOT NULL,
    bairro character varying(100) NOT NULL,
    cidade character varying(100) NOT NULL,
    estado character varying(2) NOT NULL,
    numero character varying(50) NOT NULL
);
 !   DROP TABLE public.core_endereco;
       public            postgres    false            �            1259    27271    core_endereco_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_endereco_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.core_endereco_id_seq;
       public          postgres    false    232            \           0    0    core_endereco_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.core_endereco_id_seq OWNED BY public.core_endereco.id;
          public          postgres    false    231            �            1259    27284    core_escala    TABLE     �   CREATE TABLE public.core_escala (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    dia date NOT NULL,
    "departamentoProfissional_id" integer NOT NULL
);
    DROP TABLE public.core_escala;
       public            postgres    false            �            1259    27282    core_escala_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_escala_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.core_escala_id_seq;
       public          postgres    false    234            ]           0    0    core_escala_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.core_escala_id_seq OWNED BY public.core_escala.id;
          public          postgres    false    233                        1259    27395    core_escalaintervalo    TABLE     +  CREATE TABLE public.core_escalaintervalo (
    id integer NOT NULL,
    inicio time without time zone NOT NULL,
    fim time without time zone NOT NULL,
    descricao character varying(255) NOT NULL,
    cor character varying(20) NOT NULL,
    atendimento integer,
    escala_id integer NOT NULL
);
 (   DROP TABLE public.core_escalaintervalo;
       public            postgres    false            �            1259    27393    core_escalaintervalo_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_escalaintervalo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.core_escalaintervalo_id_seq;
       public          postgres    false    256            ^           0    0    core_escalaintervalo_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.core_escalaintervalo_id_seq OWNED BY public.core_escalaintervalo.id;
          public          postgres    false    255            �            1259    27292    core_latlng    TABLE     �   CREATE TABLE public.core_latlng (
    id integer NOT NULL,
    lat double precision NOT NULL,
    lng double precision NOT NULL
);
    DROP TABLE public.core_latlng;
       public            postgres    false            �            1259    27290    core_latlng_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_latlng_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.core_latlng_id_seq;
       public          postgres    false    236            _           0    0    core_latlng_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.core_latlng_id_seq OWNED BY public.core_latlng.id;
          public          postgres    false    235            �            1259    27300    core_paciente    TABLE     �  CREATE TABLE public.core_paciente (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(80) NOT NULL,
    mae character varying(80),
    email character varying(255) NOT NULL,
    data_nascimento date NOT NULL,
    cpf character varying(14) NOT NULL,
    rg character varying(9) NOT NULL,
    idade integer NOT NULL,
    telefone character varying(40) NOT NULL,
    genero integer NOT NULL,
    sobre character varying(255) NOT NULL,
    cliente_app character varying(255) NOT NULL,
    departamento_id integer NOT NULL,
    endereco_id integer
);
 !   DROP TABLE public.core_paciente;
       public            postgres    false            �            1259    27298    core_paciente_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_paciente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.core_paciente_id_seq;
       public          postgres    false    238            `           0    0    core_paciente_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.core_paciente_id_seq OWNED BY public.core_paciente.id;
          public          postgres    false    237            �            1259    27311 %   core_pacientedepartamentoprofissional    TABLE       CREATE TABLE public.core_pacientedepartamentoprofissional (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    "departamentoProfissional_id" integer NOT NULL,
    paciente_id integer NOT NULL
);
 9   DROP TABLE public.core_pacientedepartamentoprofissional;
       public            postgres    false            �            1259    27309 ,   core_pacientedepartamentoprofissional_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_pacientedepartamentoprofissional_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 C   DROP SEQUENCE public.core_pacientedepartamentoprofissional_id_seq;
       public          postgres    false    240            a           0    0 ,   core_pacientedepartamentoprofissional_id_seq    SEQUENCE OWNED BY     }   ALTER SEQUENCE public.core_pacientedepartamentoprofissional_id_seq OWNED BY public.core_pacientedepartamentoprofissional.id;
          public          postgres    false    239            �            1259    27370    core_profissional    TABLE     �  CREATE TABLE public.core_profissional (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(255) NOT NULL,
    codigo character varying(10) NOT NULL,
    usuario character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    senha character varying(255) NOT NULL,
    ativo boolean NOT NULL,
    perfil_id integer NOT NULL,
    user_id integer NOT NULL
);
 %   DROP TABLE public.core_profissional;
       public            postgres    false            �            1259    27368    core_profissional_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_profissional_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.core_profissional_id_seq;
       public          postgres    false    252            b           0    0    core_profissional_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.core_profissional_id_seq OWNED BY public.core_profissional.id;
          public          postgres    false    251            �            1259    27387 #   core_profissional_tiposAtendimentos    TABLE     �   CREATE TABLE public."core_profissional_tiposAtendimentos" (
    id integer NOT NULL,
    profissional_id integer NOT NULL,
    atendimentosdepartamento_id integer NOT NULL
);
 9   DROP TABLE public."core_profissional_tiposAtendimentos";
       public            postgres    false            �            1259    27385 *   core_profissional_tiposAtendimentos_id_seq    SEQUENCE     �   CREATE SEQUENCE public."core_profissional_tiposAtendimentos_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 C   DROP SEQUENCE public."core_profissional_tiposAtendimentos_id_seq";
       public          postgres    false    254            c           0    0 *   core_profissional_tiposAtendimentos_id_seq    SEQUENCE OWNED BY     }   ALTER SEQUENCE public."core_profissional_tiposAtendimentos_id_seq" OWNED BY public."core_profissional_tiposAtendimentos".id;
          public          postgres    false    253            �            1259    27360    core_prontuario    TABLE     5  CREATE TABLE public.core_prontuario (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    observacao character varying(255) NOT NULL,
    atendimento_id integer NOT NULL,
    departamento_profissional_paciente_id integer NOT NULL
);
 #   DROP TABLE public.core_prontuario;
       public            postgres    false            �            1259    27358    core_prontuario_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_prontuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.core_prontuario_id_seq;
       public          postgres    false    250            d           0    0    core_prontuario_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.core_prontuario_id_seq OWNED BY public.core_prontuario.id;
          public          postgres    false    249            �            1259    27344    core_tipoatendimento    TABLE       CREATE TABLE public.core_tipoatendimento (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    descricao character varying(255) NOT NULL,
    tipo_profissional_id integer NOT NULL
);
 (   DROP TABLE public.core_tipoatendimento;
       public            postgres    false            �            1259    27352 $   core_tipoatendimento_areaAtendimento    TABLE     �   CREATE TABLE public."core_tipoatendimento_areaAtendimento" (
    id integer NOT NULL,
    tipoatendimento_id integer NOT NULL,
    areaatendimento_id integer NOT NULL
);
 :   DROP TABLE public."core_tipoatendimento_areaAtendimento";
       public            postgres    false            �            1259    27350 +   core_tipoatendimento_areaAtendimento_id_seq    SEQUENCE     �   CREATE SEQUENCE public."core_tipoatendimento_areaAtendimento_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 D   DROP SEQUENCE public."core_tipoatendimento_areaAtendimento_id_seq";
       public          postgres    false    248            e           0    0 +   core_tipoatendimento_areaAtendimento_id_seq    SEQUENCE OWNED BY        ALTER SEQUENCE public."core_tipoatendimento_areaAtendimento_id_seq" OWNED BY public."core_tipoatendimento_areaAtendimento".id;
          public          postgres    false    247            �            1259    27342    core_tipoatendimento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_tipoatendimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.core_tipoatendimento_id_seq;
       public          postgres    false    246            f           0    0    core_tipoatendimento_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.core_tipoatendimento_id_seq OWNED BY public.core_tipoatendimento.id;
          public          postgres    false    245            �            1259    27336    core_tipoprofissional    TABLE       CREATE TABLE public.core_tipoprofissional (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    descricao character varying(255) NOT NULL,
    "areaAtendimento_id" integer NOT NULL
);
 )   DROP TABLE public.core_tipoprofissional;
       public            postgres    false            �            1259    27334    core_tipoprofissional_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_tipoprofissional_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.core_tipoprofissional_id_seq;
       public          postgres    false    244            g           0    0    core_tipoprofissional_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.core_tipoprofissional_id_seq OWNED BY public.core_tipoprofissional.id;
          public          postgres    false    243            �            1259    27319    core_userprofile    TABLE     �  CREATE TABLE public.core_userprofile (
    id integer NOT NULL,
    data_cadastro timestamp with time zone NOT NULL,
    date_modificado timestamp with time zone,
    nome character varying(255) NOT NULL,
    usuario character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    senha character varying(255) NOT NULL,
    ativo boolean NOT NULL,
    departamento_id integer,
    empresa_id integer,
    perfil_id integer NOT NULL,
    user_id integer NOT NULL
);
 $   DROP TABLE public.core_userprofile;
       public            postgres    false            �            1259    27317    core_userprofile_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_userprofile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.core_userprofile_id_seq;
       public          postgres    false    242            h           0    0    core_userprofile_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.core_userprofile_id_seq OWNED BY public.core_userprofile.id;
          public          postgres    false    241            �            1259    27153    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public            postgres    false            �            1259    27151    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    213            i           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    212            �            1259    27039    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public            postgres    false            �            1259    27037    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    199            j           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    198            �            1259    27028    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public            postgres    false            �            1259    27026    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    197            k           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    196                       1259    27693    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public            postgres    false            �           2604    27060    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �           2604    27070    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    204    205            �           2604    27052    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    201    200    201            �           2604    27078    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    207    207            �           2604    27088    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            �           2604    27096    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    211    211            �           2604    27207    core_areaatendimento id    DEFAULT     �   ALTER TABLE ONLY public.core_areaatendimento ALTER COLUMN id SET DEFAULT nextval('public.core_areaatendimento_id_seq'::regclass);
 F   ALTER TABLE public.core_areaatendimento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            �           2604    27493    core_atendente id    DEFAULT     v   ALTER TABLE ONLY public.core_atendente ALTER COLUMN id SET DEFAULT nextval('public.core_atendente_id_seq'::regclass);
 @   ALTER TABLE public.core_atendente ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    259    260    260            �           2604    27215    core_atendimento id    DEFAULT     z   ALTER TABLE ONLY public.core_atendimento ALTER COLUMN id SET DEFAULT nextval('public.core_atendimento_id_seq'::regclass);
 B   ALTER TABLE public.core_atendimento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            �           2604    27223     core_atendimentosdepartamento id    DEFAULT     �   ALTER TABLE ONLY public.core_atendimentosdepartamento ALTER COLUMN id SET DEFAULT nextval('public.core_atendimentosdepartamento_id_seq'::regclass);
 O   ALTER TABLE public.core_atendimentosdepartamento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    27431    core_cliente id    DEFAULT     r   ALTER TABLE ONLY public.core_cliente ALTER COLUMN id SET DEFAULT nextval('public.core_cliente_id_seq'::regclass);
 >   ALTER TABLE public.core_cliente ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    258    257    258            �           2604    27231    core_convenio id    DEFAULT     t   ALTER TABLE ONLY public.core_convenio ALTER COLUMN id SET DEFAULT nextval('public.core_convenio_id_seq'::regclass);
 ?   ALTER TABLE public.core_convenio ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    27239    core_departamento id    DEFAULT     |   ALTER TABLE ONLY public.core_departamento ALTER COLUMN id SET DEFAULT nextval('public.core_departamento_id_seq'::regclass);
 C   ALTER TABLE public.core_departamento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            �           2604    27250     core_departamentoprofissional id    DEFAULT     �   ALTER TABLE ONLY public.core_departamentoprofissional ALTER COLUMN id SET DEFAULT nextval('public.core_departamentoprofissional_id_seq'::regclass);
 O   ALTER TABLE public.core_departamentoprofissional ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    225    226    226            �           2604    27258    core_empresa id    DEFAULT     r   ALTER TABLE ONLY public.core_empresa ALTER COLUMN id SET DEFAULT nextval('public.core_empresa_id_seq'::regclass);
 >   ALTER TABLE public.core_empresa ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227    228            �           2604    27268    core_empresa_convenios id    DEFAULT     �   ALTER TABLE ONLY public.core_empresa_convenios ALTER COLUMN id SET DEFAULT nextval('public.core_empresa_convenios_id_seq'::regclass);
 H   ALTER TABLE public.core_empresa_convenios ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    230    230            �           2604    27276    core_endereco id    DEFAULT     t   ALTER TABLE ONLY public.core_endereco ALTER COLUMN id SET DEFAULT nextval('public.core_endereco_id_seq'::regclass);
 ?   ALTER TABLE public.core_endereco ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    232    231    232            �           2604    27287    core_escala id    DEFAULT     p   ALTER TABLE ONLY public.core_escala ALTER COLUMN id SET DEFAULT nextval('public.core_escala_id_seq'::regclass);
 =   ALTER TABLE public.core_escala ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    233    234    234            �           2604    27398    core_escalaintervalo id    DEFAULT     �   ALTER TABLE ONLY public.core_escalaintervalo ALTER COLUMN id SET DEFAULT nextval('public.core_escalaintervalo_id_seq'::regclass);
 F   ALTER TABLE public.core_escalaintervalo ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    256    255    256            �           2604    27295    core_latlng id    DEFAULT     p   ALTER TABLE ONLY public.core_latlng ALTER COLUMN id SET DEFAULT nextval('public.core_latlng_id_seq'::regclass);
 =   ALTER TABLE public.core_latlng ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    235    236    236            �           2604    27303    core_paciente id    DEFAULT     t   ALTER TABLE ONLY public.core_paciente ALTER COLUMN id SET DEFAULT nextval('public.core_paciente_id_seq'::regclass);
 ?   ALTER TABLE public.core_paciente ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    238    238            �           2604    27314 (   core_pacientedepartamentoprofissional id    DEFAULT     �   ALTER TABLE ONLY public.core_pacientedepartamentoprofissional ALTER COLUMN id SET DEFAULT nextval('public.core_pacientedepartamentoprofissional_id_seq'::regclass);
 W   ALTER TABLE public.core_pacientedepartamentoprofissional ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    239    240    240            �           2604    27373    core_profissional id    DEFAULT     |   ALTER TABLE ONLY public.core_profissional ALTER COLUMN id SET DEFAULT nextval('public.core_profissional_id_seq'::regclass);
 C   ALTER TABLE public.core_profissional ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    252    251    252            �           2604    27390 &   core_profissional_tiposAtendimentos id    DEFAULT     �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos" ALTER COLUMN id SET DEFAULT nextval('public."core_profissional_tiposAtendimentos_id_seq"'::regclass);
 W   ALTER TABLE public."core_profissional_tiposAtendimentos" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    254    253    254            �           2604    27363    core_prontuario id    DEFAULT     x   ALTER TABLE ONLY public.core_prontuario ALTER COLUMN id SET DEFAULT nextval('public.core_prontuario_id_seq'::regclass);
 A   ALTER TABLE public.core_prontuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    250    249    250            �           2604    27347    core_tipoatendimento id    DEFAULT     �   ALTER TABLE ONLY public.core_tipoatendimento ALTER COLUMN id SET DEFAULT nextval('public.core_tipoatendimento_id_seq'::regclass);
 F   ALTER TABLE public.core_tipoatendimento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    245    246    246            �           2604    27355 '   core_tipoatendimento_areaAtendimento id    DEFAULT     �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento" ALTER COLUMN id SET DEFAULT nextval('public."core_tipoatendimento_areaAtendimento_id_seq"'::regclass);
 X   ALTER TABLE public."core_tipoatendimento_areaAtendimento" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    247    248    248            �           2604    27339    core_tipoprofissional id    DEFAULT     �   ALTER TABLE ONLY public.core_tipoprofissional ALTER COLUMN id SET DEFAULT nextval('public.core_tipoprofissional_id_seq'::regclass);
 G   ALTER TABLE public.core_tipoprofissional ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    243    244    244            �           2604    27322    core_userprofile id    DEFAULT     z   ALTER TABLE ONLY public.core_userprofile ALTER COLUMN id SET DEFAULT nextval('public.core_userprofile_id_seq'::regclass);
 B   ALTER TABLE public.core_userprofile ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    241    242    242            �           2604    27156    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    213    213            �           2604    27042    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    199    198    199            �           2604    27031    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    196    197    197                      0    27057 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    203   z                0    27067    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    205   �      	          0    27049    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    201   �                0    27075 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    207   �                0    27085    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    209   �                0    27093    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    211   �                0    27184    authtoken_token 
   TABLE DATA           @   COPY public.authtoken_token (key, created, user_id) FROM stdin;
    public          postgres    false    214   �                0    27204    core_areaatendimento 
   TABLE DATA           =   COPY public.core_areaatendimento (id, descricao) FROM stdin;
    public          postgres    false    216   �      D          0    27490    core_atendente 
   TABLE DATA           �   COPY public.core_atendente (id, data_cadastro, date_modificado, nome, usuario, email, senha, ativo, departamento_id, perfil_id, user_id) FROM stdin;
    public          postgres    false    260                   0    27212    core_atendimento 
   TABLE DATA           �   COPY public.core_atendimento (id, data_cadastro, date_modificado, retorno, valor, tempo, inicio_atendimento, fim_atendimento, pago, crm_soliciante, "departamentoProfissional_id", intervalo_id, paciente_id, "tipoAtendimento_id") FROM stdin;
    public          postgres    false    218   4                0    27220    core_atendimentosdepartamento 
   TABLE DATA           �   COPY public.core_atendimentosdepartamento (id, data_cadastro, date_modificado, nome, tipo_profissional, tempo_padrao, valor_padrao, publico, departamento_id, tipo_atendimento_id) FROM stdin;
    public          postgres    false    220   Q      B          0    27428    core_cliente 
   TABLE DATA           �   COPY public.core_cliente (id, data_cadastro, date_modificado, nome, usuario, email, senha, ativo, cliente_app, perfil_id, user_id) FROM stdin;
    public          postgres    false    258   n                0    27228    core_convenio 
   TABLE DATA           f   COPY public.core_convenio (id, data_cadastro, date_modificado, nome, descricao, desconto) FROM stdin;
    public          postgres    false    222   �                 0    27236    core_departamento 
   TABLE DATA           y   COPY public.core_departamento (id, data_cadastro, date_modificado, nome, descricao, empresa_id, endereco_id) FROM stdin;
    public          postgres    false    224   �      "          0    27247    core_departamentoprofissional 
   TABLE DATA           s   COPY public.core_departamentoprofissional (id, departamento_id, profissional_id, tipo_profissional_id) FROM stdin;
    public          postgres    false    226   �      $          0    27255    core_empresa 
   TABLE DATA           h   COPY public.core_empresa (id, data_cadastro, date_modificado, nome_razao_social, documento) FROM stdin;
    public          postgres    false    228   �      &          0    27265    core_empresa_convenios 
   TABLE DATA           M   COPY public.core_empresa_convenios (id, empresa_id, convenio_id) FROM stdin;
    public          postgres    false    230   �      (          0    27273    core_endereco 
   TABLE DATA           P   COPY public.core_endereco (id, rua, bairro, cidade, estado, numero) FROM stdin;
    public          postgres    false    232         *          0    27284    core_escala 
   TABLE DATA           m   COPY public.core_escala (id, data_cadastro, date_modificado, dia, "departamentoProfissional_id") FROM stdin;
    public          postgres    false    234   9      @          0    27395    core_escalaintervalo 
   TABLE DATA           g   COPY public.core_escalaintervalo (id, inicio, fim, descricao, cor, atendimento, escala_id) FROM stdin;
    public          postgres    false    256   V      ,          0    27292    core_latlng 
   TABLE DATA           3   COPY public.core_latlng (id, lat, lng) FROM stdin;
    public          postgres    false    236   s      .          0    27300    core_paciente 
   TABLE DATA           �   COPY public.core_paciente (id, data_cadastro, date_modificado, nome, mae, email, data_nascimento, cpf, rg, idade, telefone, genero, sobre, cliente_app, departamento_id, endereco_id) FROM stdin;
    public          postgres    false    238   �      0          0    27311 %   core_pacientedepartamentoprofissional 
   TABLE DATA           �   COPY public.core_pacientedepartamentoprofissional (id, data_cadastro, date_modificado, "departamentoProfissional_id", paciente_id) FROM stdin;
    public          postgres    false    240   �      <          0    27370    core_profissional 
   TABLE DATA           �   COPY public.core_profissional (id, data_cadastro, date_modificado, nome, codigo, usuario, email, senha, ativo, perfil_id, user_id) FROM stdin;
    public          postgres    false    252   �      >          0    27387 #   core_profissional_tiposAtendimentos 
   TABLE DATA           q   COPY public."core_profissional_tiposAtendimentos" (id, profissional_id, atendimentosdepartamento_id) FROM stdin;
    public          postgres    false    254   �      :          0    27360    core_prontuario 
   TABLE DATA           �   COPY public.core_prontuario (id, data_cadastro, date_modificado, observacao, atendimento_id, departamento_profissional_paciente_id) FROM stdin;
    public          postgres    false    250         6          0    27344    core_tipoatendimento 
   TABLE DATA           s   COPY public.core_tipoatendimento (id, data_cadastro, date_modificado, descricao, tipo_profissional_id) FROM stdin;
    public          postgres    false    246   !      8          0    27352 $   core_tipoatendimento_areaAtendimento 
   TABLE DATA           l   COPY public."core_tipoatendimento_areaAtendimento" (id, tipoatendimento_id, areaatendimento_id) FROM stdin;
    public          postgres    false    248   >      4          0    27336    core_tipoprofissional 
   TABLE DATA           t   COPY public.core_tipoprofissional (id, data_cadastro, date_modificado, descricao, "areaAtendimento_id") FROM stdin;
    public          postgres    false    244   [      2          0    27319    core_userprofile 
   TABLE DATA           �   COPY public.core_userprofile (id, data_cadastro, date_modificado, nome, usuario, email, senha, ativo, departamento_id, empresa_id, perfil_id, user_id) FROM stdin;
    public          postgres    false    242   x                0    27153    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    213   �                0    27039    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    199   s                0    27028    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    197   �      E          0    27693    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    261   �      l           0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 5, true);
          public          postgres    false    202            m           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 68, true);
          public          postgres    false    204            n           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 154, true);
          public          postgres    false    200            o           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    208            p           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);
          public          postgres    false    206            q           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    210            r           0    0    core_areaatendimento_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.core_areaatendimento_id_seq', 54, true);
          public          postgres    false    215            s           0    0    core_atendente_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.core_atendente_id_seq', 1, false);
          public          postgres    false    259            t           0    0    core_atendimento_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.core_atendimento_id_seq', 1, false);
          public          postgres    false    217            u           0    0 $   core_atendimentosdepartamento_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.core_atendimentosdepartamento_id_seq', 1, false);
          public          postgres    false    219            v           0    0    core_cliente_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.core_cliente_id_seq', 1, false);
          public          postgres    false    257            w           0    0    core_convenio_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.core_convenio_id_seq', 1, false);
          public          postgres    false    221            x           0    0    core_departamento_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.core_departamento_id_seq', 1, false);
          public          postgres    false    223            y           0    0 $   core_departamentoprofissional_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.core_departamentoprofissional_id_seq', 1, false);
          public          postgres    false    225            z           0    0    core_empresa_convenios_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.core_empresa_convenios_id_seq', 1, false);
          public          postgres    false    229            {           0    0    core_empresa_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.core_empresa_id_seq', 1, false);
          public          postgres    false    227            |           0    0    core_endereco_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.core_endereco_id_seq', 1, false);
          public          postgres    false    231            }           0    0    core_escala_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.core_escala_id_seq', 1, false);
          public          postgres    false    233            ~           0    0    core_escalaintervalo_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.core_escalaintervalo_id_seq', 1, false);
          public          postgres    false    255                       0    0    core_latlng_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.core_latlng_id_seq', 1, false);
          public          postgres    false    235            �           0    0    core_paciente_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.core_paciente_id_seq', 1, false);
          public          postgres    false    237            �           0    0 ,   core_pacientedepartamentoprofissional_id_seq    SEQUENCE SET     [   SELECT pg_catalog.setval('public.core_pacientedepartamentoprofissional_id_seq', 1, false);
          public          postgres    false    239            �           0    0    core_profissional_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.core_profissional_id_seq', 1, false);
          public          postgres    false    251            �           0    0 *   core_profissional_tiposAtendimentos_id_seq    SEQUENCE SET     [   SELECT pg_catalog.setval('public."core_profissional_tiposAtendimentos_id_seq"', 1, false);
          public          postgres    false    253            �           0    0    core_prontuario_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.core_prontuario_id_seq', 1, false);
          public          postgres    false    249            �           0    0 +   core_tipoatendimento_areaAtendimento_id_seq    SEQUENCE SET     \   SELECT pg_catalog.setval('public."core_tipoatendimento_areaAtendimento_id_seq"', 1, false);
          public          postgres    false    247            �           0    0    core_tipoatendimento_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.core_tipoatendimento_id_seq', 1, false);
          public          postgres    false    245            �           0    0    core_tipoprofissional_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.core_tipoprofissional_id_seq', 1, false);
          public          postgres    false    243            �           0    0    core_userprofile_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.core_userprofile_id_seq', 1, false);
          public          postgres    false    241            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 45, true);
          public          postgres    false    212            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 29, true);
          public          postgres    false    198            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 24, true);
          public          postgres    false    196            �           2606    27182    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    203            �           2606    27109 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    205    205            �           2606    27072 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    205            �           2606    27062    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    203            �           2606    27100 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    201    201            �           2606    27054 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    201            �           2606    27090 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    209            �           2606    27124 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    209    209            �           2606    27080    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    207            �           2606    27098 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    211            �           2606    27138 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    211    211            �           2606    27176     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    207            �           2606    27188 $   authtoken_token authtoken_token_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);
 N   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_pkey;
       public            postgres    false    214            �           2606    27190 +   authtoken_token authtoken_token_user_id_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);
 U   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_key;
       public            postgres    false    214            �           2606    27209 .   core_areaatendimento core_areaatendimento_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.core_areaatendimento
    ADD CONSTRAINT core_areaatendimento_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.core_areaatendimento DROP CONSTRAINT core_areaatendimento_pkey;
       public            postgres    false    216            N           2606    27502 '   core_atendente core_atendente_email_key 
   CONSTRAINT     c   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_email_key UNIQUE (email);
 Q   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_email_key;
       public            postgres    false    260            Q           2606    27498 "   core_atendente core_atendente_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_pkey;
       public            postgres    false    260            S           2606    27504 )   core_atendente core_atendente_user_id_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_user_id_key UNIQUE (user_id);
 S   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_user_id_key;
       public            postgres    false    260            V           2606    27500 )   core_atendente core_atendente_usuario_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_usuario_key UNIQUE (usuario);
 S   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_usuario_key;
       public            postgres    false    260            �           2606    27217 &   core_atendimento core_atendimento_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.core_atendimento
    ADD CONSTRAINT core_atendimento_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.core_atendimento DROP CONSTRAINT core_atendimento_pkey;
       public            postgres    false    218            �           2606    27225 @   core_atendimentosdepartamento core_atendimentosdepartamento_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.core_atendimentosdepartamento
    ADD CONSTRAINT core_atendimentosdepartamento_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.core_atendimentosdepartamento DROP CONSTRAINT core_atendimentosdepartamento_pkey;
       public            postgres    false    220            B           2606    27440 #   core_cliente core_cliente_email_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.core_cliente
    ADD CONSTRAINT core_cliente_email_key UNIQUE (email);
 M   ALTER TABLE ONLY public.core_cliente DROP CONSTRAINT core_cliente_email_key;
       public            postgres    false    258            E           2606    27436    core_cliente core_cliente_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.core_cliente
    ADD CONSTRAINT core_cliente_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.core_cliente DROP CONSTRAINT core_cliente_pkey;
       public            postgres    false    258            G           2606    27442 %   core_cliente core_cliente_user_id_key 
   CONSTRAINT     c   ALTER TABLE ONLY public.core_cliente
    ADD CONSTRAINT core_cliente_user_id_key UNIQUE (user_id);
 O   ALTER TABLE ONLY public.core_cliente DROP CONSTRAINT core_cliente_user_id_key;
       public            postgres    false    258            J           2606    27438 %   core_cliente core_cliente_usuario_key 
   CONSTRAINT     c   ALTER TABLE ONLY public.core_cliente
    ADD CONSTRAINT core_cliente_usuario_key UNIQUE (usuario);
 O   ALTER TABLE ONLY public.core_cliente DROP CONSTRAINT core_cliente_usuario_key;
       public            postgres    false    258            �           2606    27233     core_convenio core_convenio_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.core_convenio
    ADD CONSTRAINT core_convenio_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.core_convenio DROP CONSTRAINT core_convenio_pkey;
       public            postgres    false    222            �           2606    27244 (   core_departamento core_departamento_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.core_departamento
    ADD CONSTRAINT core_departamento_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.core_departamento DROP CONSTRAINT core_departamento_pkey;
       public            postgres    false    224            �           2606    27252 @   core_departamentoprofissional core_departamentoprofissional_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.core_departamentoprofissional
    ADD CONSTRAINT core_departamentoprofissional_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.core_departamentoprofissional DROP CONSTRAINT core_departamentoprofissional_pkey;
       public            postgres    false    226            �           2606    27513 R   core_empresa_convenios core_empresa_convenios_empresa_id_convenio_id_8d4a56db_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_empresa_convenios
    ADD CONSTRAINT core_empresa_convenios_empresa_id_convenio_id_8d4a56db_uniq UNIQUE (empresa_id, convenio_id);
 |   ALTER TABLE ONLY public.core_empresa_convenios DROP CONSTRAINT core_empresa_convenios_empresa_id_convenio_id_8d4a56db_uniq;
       public            postgres    false    230    230            �           2606    27270 2   core_empresa_convenios core_empresa_convenios_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.core_empresa_convenios
    ADD CONSTRAINT core_empresa_convenios_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.core_empresa_convenios DROP CONSTRAINT core_empresa_convenios_pkey;
       public            postgres    false    230            �           2606    27262 '   core_empresa core_empresa_documento_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.core_empresa
    ADD CONSTRAINT core_empresa_documento_key UNIQUE (documento);
 Q   ALTER TABLE ONLY public.core_empresa DROP CONSTRAINT core_empresa_documento_key;
       public            postgres    false    228            �           2606    27260    core_empresa core_empresa_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.core_empresa
    ADD CONSTRAINT core_empresa_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.core_empresa DROP CONSTRAINT core_empresa_pkey;
       public            postgres    false    228                        2606    27281     core_endereco core_endereco_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.core_endereco
    ADD CONSTRAINT core_endereco_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.core_endereco DROP CONSTRAINT core_endereco_pkey;
       public            postgres    false    232                       2606    27289    core_escala core_escala_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.core_escala
    ADD CONSTRAINT core_escala_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.core_escala DROP CONSTRAINT core_escala_pkey;
       public            postgres    false    234            ?           2606    27400 .   core_escalaintervalo core_escalaintervalo_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.core_escalaintervalo
    ADD CONSTRAINT core_escalaintervalo_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.core_escalaintervalo DROP CONSTRAINT core_escalaintervalo_pkey;
       public            postgres    false    256                       2606    27297    core_latlng core_latlng_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.core_latlng
    ADD CONSTRAINT core_latlng_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.core_latlng DROP CONSTRAINT core_latlng_pkey;
       public            postgres    false    236            	           2606    27308     core_paciente core_paciente_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.core_paciente
    ADD CONSTRAINT core_paciente_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.core_paciente DROP CONSTRAINT core_paciente_pkey;
       public            postgres    false    238                       2606    27316 P   core_pacientedepartamentoprofissional core_pacientedepartamentoprofissional_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_pacientedepartamentoprofissional
    ADD CONSTRAINT core_pacientedepartamentoprofissional_pkey PRIMARY KEY (id);
 z   ALTER TABLE ONLY public.core_pacientedepartamentoprofissional DROP CONSTRAINT core_pacientedepartamentoprofissional_pkey;
       public            postgres    false    240            .           2606    27382 -   core_profissional core_profissional_email_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.core_profissional
    ADD CONSTRAINT core_profissional_email_key UNIQUE (email);
 W   ALTER TABLE ONLY public.core_profissional DROP CONSTRAINT core_profissional_email_key;
       public            postgres    false    252            1           2606    27378 (   core_profissional core_profissional_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.core_profissional
    ADD CONSTRAINT core_profissional_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.core_profissional DROP CONSTRAINT core_profissional_pkey;
       public            postgres    false    252            8           2606    27632 c   core_profissional_tiposAtendimentos core_profissional_tiposA_profissional_id_atendime_23e55266_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos"
    ADD CONSTRAINT "core_profissional_tiposA_profissional_id_atendime_23e55266_uniq" UNIQUE (profissional_id, atendimentosdepartamento_id);
 �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos" DROP CONSTRAINT "core_profissional_tiposA_profissional_id_atendime_23e55266_uniq";
       public            postgres    false    254    254            ;           2606    27392 L   core_profissional_tiposAtendimentos core_profissional_tiposAtendimentos_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos"
    ADD CONSTRAINT "core_profissional_tiposAtendimentos_pkey" PRIMARY KEY (id);
 z   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos" DROP CONSTRAINT "core_profissional_tiposAtendimentos_pkey";
       public            postgres    false    254            3           2606    27384 /   core_profissional core_profissional_user_id_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.core_profissional
    ADD CONSTRAINT core_profissional_user_id_key UNIQUE (user_id);
 Y   ALTER TABLE ONLY public.core_profissional DROP CONSTRAINT core_profissional_user_id_key;
       public            postgres    false    252            6           2606    27380 /   core_profissional core_profissional_usuario_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.core_profissional
    ADD CONSTRAINT core_profissional_usuario_key UNIQUE (usuario);
 Y   ALTER TABLE ONLY public.core_profissional DROP CONSTRAINT core_profissional_usuario_key;
       public            postgres    false    252            (           2606    27367 2   core_prontuario core_prontuario_atendimento_id_key 
   CONSTRAINT     w   ALTER TABLE ONLY public.core_prontuario
    ADD CONSTRAINT core_prontuario_atendimento_id_key UNIQUE (atendimento_id);
 \   ALTER TABLE ONLY public.core_prontuario DROP CONSTRAINT core_prontuario_atendimento_id_key;
       public            postgres    false    250            +           2606    27365 $   core_prontuario core_prontuario_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.core_prontuario
    ADD CONSTRAINT core_prontuario_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.core_prontuario DROP CONSTRAINT core_prontuario_pkey;
       public            postgres    false    250            "           2606    27594 d   core_tipoatendimento_areaAtendimento core_tipoatendimento_are_tipoatendimento_id_areaa_14ea2866_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento"
    ADD CONSTRAINT core_tipoatendimento_are_tipoatendimento_id_areaa_14ea2866_uniq UNIQUE (tipoatendimento_id, areaatendimento_id);
 �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento" DROP CONSTRAINT core_tipoatendimento_are_tipoatendimento_id_areaa_14ea2866_uniq;
       public            postgres    false    248    248            &           2606    27357 N   core_tipoatendimento_areaAtendimento core_tipoatendimento_areaAtendimento_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento"
    ADD CONSTRAINT "core_tipoatendimento_areaAtendimento_pkey" PRIMARY KEY (id);
 |   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento" DROP CONSTRAINT "core_tipoatendimento_areaAtendimento_pkey";
       public            postgres    false    248                       2606    27349 .   core_tipoatendimento core_tipoatendimento_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.core_tipoatendimento
    ADD CONSTRAINT core_tipoatendimento_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.core_tipoatendimento DROP CONSTRAINT core_tipoatendimento_pkey;
       public            postgres    false    246                       2606    27341 0   core_tipoprofissional core_tipoprofissional_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.core_tipoprofissional
    ADD CONSTRAINT core_tipoprofissional_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.core_tipoprofissional DROP CONSTRAINT core_tipoprofissional_pkey;
       public            postgres    false    244                       2606    27331 +   core_userprofile core_userprofile_email_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_email_key UNIQUE (email);
 U   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_email_key;
       public            postgres    false    242                       2606    27327 &   core_userprofile core_userprofile_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_pkey;
       public            postgres    false    242                       2606    27333 -   core_userprofile core_userprofile_user_id_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_user_id_key UNIQUE (user_id);
 W   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_user_id_key;
       public            postgres    false    242                       2606    27329 -   core_userprofile core_userprofile_usuario_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_usuario_key UNIQUE (usuario);
 W   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_usuario_key;
       public            postgres    false    242            �           2606    27162 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    213            �           2606    27046 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    199    199            �           2606    27044 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    199            �           2606    27036 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    197            Y           2606    27700 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    261            �           1259    27183    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    203            �           1259    27120 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    205            �           1259    27121 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    205            �           1259    27106 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    201            �           1259    27136 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    209            �           1259    27135 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    209            �           1259    27150 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    211            �           1259    27149 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    211            �           1259    27177     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    207            �           1259    27196 !   authtoken_token_key_10f0b77e_like    INDEX     p   CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);
 5   DROP INDEX public.authtoken_token_key_10f0b77e_like;
       public            postgres    false    214            K           1259    27691 '   core_atendente_departamento_id_0e963d91    INDEX     m   CREATE INDEX core_atendente_departamento_id_0e963d91 ON public.core_atendente USING btree (departamento_id);
 ;   DROP INDEX public.core_atendente_departamento_id_0e963d91;
       public            postgres    false    260            L           1259    27690 "   core_atendente_email_1ff45d25_like    INDEX     r   CREATE INDEX core_atendente_email_1ff45d25_like ON public.core_atendente USING btree (email varchar_pattern_ops);
 6   DROP INDEX public.core_atendente_email_1ff45d25_like;
       public            postgres    false    260            O           1259    27692 !   core_atendente_perfil_id_83961c48    INDEX     a   CREATE INDEX core_atendente_perfil_id_83961c48 ON public.core_atendente USING btree (perfil_id);
 5   DROP INDEX public.core_atendente_perfil_id_83961c48;
       public            postgres    false    260            T           1259    27689 $   core_atendente_usuario_0644abeb_like    INDEX     v   CREATE INDEX core_atendente_usuario_0644abeb_like ON public.core_atendente USING btree (usuario varchar_pattern_ops);
 8   DROP INDEX public.core_atendente_usuario_0644abeb_like;
       public            postgres    false    260            �           1259    27670 5   core_atendimento_departamentoProfissional_id_34ba6f08    INDEX     �   CREATE INDEX "core_atendimento_departamentoProfissional_id_34ba6f08" ON public.core_atendimento USING btree ("departamentoProfissional_id");
 K   DROP INDEX public."core_atendimento_departamentoProfissional_id_34ba6f08";
       public            postgres    false    218            �           1259    27671 &   core_atendimento_intervalo_id_7ae58d0b    INDEX     k   CREATE INDEX core_atendimento_intervalo_id_7ae58d0b ON public.core_atendimento USING btree (intervalo_id);
 :   DROP INDEX public.core_atendimento_intervalo_id_7ae58d0b;
       public            postgres    false    218            �           1259    27672 %   core_atendimento_paciente_id_d4144421    INDEX     i   CREATE INDEX core_atendimento_paciente_id_d4144421 ON public.core_atendimento USING btree (paciente_id);
 9   DROP INDEX public.core_atendimento_paciente_id_d4144421;
       public            postgres    false    218            �           1259    27673 ,   core_atendimento_tipoAtendimento_id_cd231362    INDEX     {   CREATE INDEX "core_atendimento_tipoAtendimento_id_cd231362" ON public.core_atendimento USING btree ("tipoAtendimento_id");
 B   DROP INDEX public."core_atendimento_tipoAtendimento_id_cd231362";
       public            postgres    false    218            �           1259    27668 6   core_atendimentosdepartamento_departamento_id_712e5126    INDEX     �   CREATE INDEX core_atendimentosdepartamento_departamento_id_712e5126 ON public.core_atendimentosdepartamento USING btree (departamento_id);
 J   DROP INDEX public.core_atendimentosdepartamento_departamento_id_712e5126;
       public            postgres    false    220            �           1259    27669 :   core_atendimentosdepartamento_tipo_atendimento_id_0d866dd2    INDEX     �   CREATE INDEX core_atendimentosdepartamento_tipo_atendimento_id_0d866dd2 ON public.core_atendimentosdepartamento USING btree (tipo_atendimento_id);
 N   DROP INDEX public.core_atendimentosdepartamento_tipo_atendimento_id_0d866dd2;
       public            postgres    false    220            @           1259    27666     core_cliente_email_d4cc05a2_like    INDEX     n   CREATE INDEX core_cliente_email_d4cc05a2_like ON public.core_cliente USING btree (email varchar_pattern_ops);
 4   DROP INDEX public.core_cliente_email_d4cc05a2_like;
       public            postgres    false    258            C           1259    27667    core_cliente_perfil_id_1c9cc5bf    INDEX     ]   CREATE INDEX core_cliente_perfil_id_1c9cc5bf ON public.core_cliente USING btree (perfil_id);
 3   DROP INDEX public.core_cliente_perfil_id_1c9cc5bf;
       public            postgres    false    258            H           1259    27665 "   core_cliente_usuario_f7f8d44c_like    INDEX     r   CREATE INDEX core_cliente_usuario_f7f8d44c_like ON public.core_cliente USING btree (usuario varchar_pattern_ops);
 6   DROP INDEX public.core_cliente_usuario_f7f8d44c_like;
       public            postgres    false    258            �           1259    27653 %   core_departamento_empresa_id_b18cc9c8    INDEX     i   CREATE INDEX core_departamento_empresa_id_b18cc9c8 ON public.core_departamento USING btree (empresa_id);
 9   DROP INDEX public.core_departamento_empresa_id_b18cc9c8;
       public            postgres    false    224            �           1259    27654 &   core_departamento_endereco_id_30b5f269    INDEX     k   CREATE INDEX core_departamento_endereco_id_30b5f269 ON public.core_departamento USING btree (endereco_id);
 :   DROP INDEX public.core_departamento_endereco_id_30b5f269;
       public            postgres    false    224            �           1259    27510 6   core_departamentoprofissional_departamento_id_d0d6a1db    INDEX     �   CREATE INDEX core_departamentoprofissional_departamento_id_d0d6a1db ON public.core_departamentoprofissional USING btree (departamento_id);
 J   DROP INDEX public.core_departamentoprofissional_departamento_id_d0d6a1db;
       public            postgres    false    226            �           1259    27651 6   core_departamentoprofissional_profissional_id_b11f772e    INDEX     �   CREATE INDEX core_departamentoprofissional_profissional_id_b11f772e ON public.core_departamentoprofissional USING btree (profissional_id);
 J   DROP INDEX public.core_departamentoprofissional_profissional_id_b11f772e;
       public            postgres    false    226            �           1259    27652 ;   core_departamentoprofissional_tipo_profissional_id_8dc7c694    INDEX     �   CREATE INDEX core_departamentoprofissional_tipo_profissional_id_8dc7c694 ON public.core_departamentoprofissional USING btree (tipo_profissional_id);
 O   DROP INDEX public.core_departamentoprofissional_tipo_profissional_id_8dc7c694;
       public            postgres    false    226            �           1259    27525 +   core_empresa_convenios_convenio_id_eadb805d    INDEX     u   CREATE INDEX core_empresa_convenios_convenio_id_eadb805d ON public.core_empresa_convenios USING btree (convenio_id);
 ?   DROP INDEX public.core_empresa_convenios_convenio_id_eadb805d;
       public            postgres    false    230            �           1259    27524 *   core_empresa_convenios_empresa_id_429984f9    INDEX     s   CREATE INDEX core_empresa_convenios_empresa_id_429984f9 ON public.core_empresa_convenios USING btree (empresa_id);
 >   DROP INDEX public.core_empresa_convenios_empresa_id_429984f9;
       public            postgres    false    230            �           1259    27511 $   core_empresa_documento_78c94a92_like    INDEX     v   CREATE INDEX core_empresa_documento_78c94a92_like ON public.core_empresa USING btree (documento varchar_pattern_ops);
 8   DROP INDEX public.core_empresa_documento_78c94a92_like;
       public            postgres    false    228                       1259    27531 0   core_escala_departamentoProfissional_id_baa53877    INDEX     �   CREATE INDEX "core_escala_departamentoProfissional_id_baa53877" ON public.core_escala USING btree ("departamentoProfissional_id");
 F   DROP INDEX public."core_escala_departamentoProfissional_id_baa53877";
       public            postgres    false    234            =           1259    27650 '   core_escalaintervalo_escala_id_dc032186    INDEX     m   CREATE INDEX core_escalaintervalo_escala_id_dc032186 ON public.core_escalaintervalo USING btree (escala_id);
 ;   DROP INDEX public.core_escalaintervalo_escala_id_dc032186;
       public            postgres    false    256                       1259    27542 &   core_paciente_departamento_id_982e887a    INDEX     k   CREATE INDEX core_paciente_departamento_id_982e887a ON public.core_paciente USING btree (departamento_id);
 :   DROP INDEX public.core_paciente_departamento_id_982e887a;
       public            postgres    false    238                       1259    27543 "   core_paciente_endereco_id_20370ab8    INDEX     c   CREATE INDEX core_paciente_endereco_id_20370ab8 ON public.core_paciente USING btree (endereco_id);
 6   DROP INDEX public.core_paciente_endereco_id_20370ab8;
       public            postgres    false    238            
           1259    27554 >   core_pacientedepartamentop_departamentoProfissional_i_94d9e572    INDEX     �   CREATE INDEX "core_pacientedepartamentop_departamentoProfissional_i_94d9e572" ON public.core_pacientedepartamentoprofissional USING btree ("departamentoProfissional_id");
 T   DROP INDEX public."core_pacientedepartamentop_departamentoProfissional_i_94d9e572";
       public            postgres    false    240                       1259    27555 :   core_pacientedepartamentoprofissional_paciente_id_f0753164    INDEX     �   CREATE INDEX core_pacientedepartamentoprofissional_paciente_id_f0753164 ON public.core_pacientedepartamentoprofissional USING btree (paciente_id);
 N   DROP INDEX public.core_pacientedepartamentoprofissional_paciente_id_f0753164;
       public            postgres    false    240            ,           1259    27629 %   core_profissional_email_e79cdb8d_like    INDEX     x   CREATE INDEX core_profissional_email_e79cdb8d_like ON public.core_profissional USING btree (email varchar_pattern_ops);
 9   DROP INDEX public.core_profissional_email_e79cdb8d_like;
       public            postgres    false    252            /           1259    27630 $   core_profissional_perfil_id_be73e1c3    INDEX     g   CREATE INDEX core_profissional_perfil_id_be73e1c3 ON public.core_profissional USING btree (perfil_id);
 8   DROP INDEX public.core_profissional_perfil_id_be73e1c3;
       public            postgres    false    252            9           1259    27644 >   core_profissional_tiposAte_atendimentosdepartamento_i_9f600534    INDEX     �   CREATE INDEX "core_profissional_tiposAte_atendimentosdepartamento_i_9f600534" ON public."core_profissional_tiposAtendimentos" USING btree (atendimentosdepartamento_id);
 T   DROP INDEX public."core_profissional_tiposAte_atendimentosdepartamento_i_9f600534";
       public            postgres    false    254            <           1259    27643 <   core_profissional_tiposAtendimentos_profissional_id_ff4fe485    INDEX     �   CREATE INDEX "core_profissional_tiposAtendimentos_profissional_id_ff4fe485" ON public."core_profissional_tiposAtendimentos" USING btree (profissional_id);
 R   DROP INDEX public."core_profissional_tiposAtendimentos_profissional_id_ff4fe485";
       public            postgres    false    254            4           1259    27628 '   core_profissional_usuario_c7856ecf_like    INDEX     |   CREATE INDEX core_profissional_usuario_c7856ecf_like ON public.core_profissional USING btree (usuario varchar_pattern_ops);
 ;   DROP INDEX public.core_profissional_usuario_c7856ecf_like;
       public            postgres    false    252            )           1259    27617 >   core_prontuario_departamento_profissional_paciente_id_46b458ef    INDEX     �   CREATE INDEX core_prontuario_departamento_profissional_paciente_id_46b458ef ON public.core_prontuario USING btree (departamento_profissional_paciente_id);
 R   DROP INDEX public.core_prontuario_departamento_profissional_paciente_id_46b458ef;
       public            postgres    false    250            #           1259    27606 6   core_tipoatendimento_areaA_areaatendimento_id_3bca587d    INDEX     �   CREATE INDEX "core_tipoatendimento_areaA_areaatendimento_id_3bca587d" ON public."core_tipoatendimento_areaAtendimento" USING btree (areaatendimento_id);
 L   DROP INDEX public."core_tipoatendimento_areaA_areaatendimento_id_3bca587d";
       public            postgres    false    248            $           1259    27605 6   core_tipoatendimento_areaA_tipoatendimento_id_e3b147b0    INDEX     �   CREATE INDEX "core_tipoatendimento_areaA_tipoatendimento_id_e3b147b0" ON public."core_tipoatendimento_areaAtendimento" USING btree (tipoatendimento_id);
 L   DROP INDEX public."core_tipoatendimento_areaA_tipoatendimento_id_e3b147b0";
       public            postgres    false    248                        1259    27592 2   core_tipoatendimento_tipo_profissional_id_b1e19a65    INDEX     �   CREATE INDEX core_tipoatendimento_tipo_profissional_id_b1e19a65 ON public.core_tipoatendimento USING btree (tipo_profissional_id);
 F   DROP INDEX public.core_tipoatendimento_tipo_profissional_id_b1e19a65;
       public            postgres    false    246                       1259    27586 1   core_tipoprofissional_areaAtendimento_id_45687893    INDEX     �   CREATE INDEX "core_tipoprofissional_areaAtendimento_id_45687893" ON public.core_tipoprofissional USING btree ("areaAtendimento_id");
 G   DROP INDEX public."core_tipoprofissional_areaAtendimento_id_45687893";
       public            postgres    false    244                       1259    27578 )   core_userprofile_departamento_id_14963af2    INDEX     q   CREATE INDEX core_userprofile_departamento_id_14963af2 ON public.core_userprofile USING btree (departamento_id);
 =   DROP INDEX public.core_userprofile_departamento_id_14963af2;
       public            postgres    false    242                       1259    27577 $   core_userprofile_email_ba06e794_like    INDEX     v   CREATE INDEX core_userprofile_email_ba06e794_like ON public.core_userprofile USING btree (email varchar_pattern_ops);
 8   DROP INDEX public.core_userprofile_email_ba06e794_like;
       public            postgres    false    242                       1259    27579 $   core_userprofile_empresa_id_c5a8b4b9    INDEX     g   CREATE INDEX core_userprofile_empresa_id_c5a8b4b9 ON public.core_userprofile USING btree (empresa_id);
 8   DROP INDEX public.core_userprofile_empresa_id_c5a8b4b9;
       public            postgres    false    242                       1259    27580 #   core_userprofile_perfil_id_8ac5d178    INDEX     e   CREATE INDEX core_userprofile_perfil_id_8ac5d178 ON public.core_userprofile USING btree (perfil_id);
 7   DROP INDEX public.core_userprofile_perfil_id_8ac5d178;
       public            postgres    false    242                       1259    27576 &   core_userprofile_usuario_fa979e13_like    INDEX     z   CREATE INDEX core_userprofile_usuario_fa979e13_like ON public.core_userprofile USING btree (usuario varchar_pattern_ops);
 :   DROP INDEX public.core_userprofile_usuario_fa979e13_like;
       public            postgres    false    242            �           1259    27173 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    213            �           1259    27174 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    213            W           1259    27702 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    261            Z           1259    27701 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    261            ]           2606    27115 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    205    2999    201            \           2606    27110 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    205    203    3004            [           2606    27101 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    199    201    2994            _           2606    27130 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    203    209    3004            ^           2606    27125 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    3012    209    207            a           2606    27144 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    2999    201    211            `           2606    27139 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    3012    211    207            d           2606    27197 @   authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id;
       public          postgres    false    207    3012    214            �           2606    27674 N   core_atendente core_atendente_departamento_id_0e963d91_fk_core_departamento_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_departamento_id_0e963d91_fk_core_departamento_id FOREIGN KEY (departamento_id) REFERENCES public.core_departamento(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_departamento_id_0e963d91_fk_core_departamento_id;
       public          postgres    false    224    3054    260            �           2606    27679 A   core_atendente core_atendente_perfil_id_83961c48_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_perfil_id_83961c48_fk_auth_group_id FOREIGN KEY (perfil_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 k   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_perfil_id_83961c48_fk_auth_group_id;
       public          postgres    false    3004    203    260            �           2606    27684 >   core_atendente core_atendente_user_id_38d72987_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendente
    ADD CONSTRAINT core_atendente_user_id_38d72987_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.core_atendente DROP CONSTRAINT core_atendente_user_id_38d72987_fk_auth_user_id;
       public          postgres    false    207    260    3012            e           2606    27463 L   core_atendimento core_atendimento_departamentoProfissi_34ba6f08_fk_core_depa    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendimento
    ADD CONSTRAINT "core_atendimento_departamentoProfissi_34ba6f08_fk_core_depa" FOREIGN KEY ("departamentoProfissional_id") REFERENCES public.core_departamentoprofissional(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.core_atendimento DROP CONSTRAINT "core_atendimento_departamentoProfissi_34ba6f08_fk_core_depa";
       public          postgres    false    3057    226    218            f           2606    27468 D   core_atendimento core_atendimento_intervalo_id_7ae58d0b_fk_core_esca    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendimento
    ADD CONSTRAINT core_atendimento_intervalo_id_7ae58d0b_fk_core_esca FOREIGN KEY (intervalo_id) REFERENCES public.core_escalaintervalo(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.core_atendimento DROP CONSTRAINT core_atendimento_intervalo_id_7ae58d0b_fk_core_esca;
       public          postgres    false    3135    256    218            g           2606    27474 J   core_atendimento core_atendimento_paciente_id_d4144421_fk_core_paciente_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendimento
    ADD CONSTRAINT core_atendimento_paciente_id_d4144421_fk_core_paciente_id FOREIGN KEY (paciente_id) REFERENCES public.core_paciente(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.core_atendimento DROP CONSTRAINT core_atendimento_paciente_id_d4144421_fk_core_paciente_id;
       public          postgres    false    3081    238    218            h           2606    27483 J   core_atendimento core_atendimento_tipoAtendimento_id_cd231362_fk_core_aten    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendimento
    ADD CONSTRAINT "core_atendimento_tipoAtendimento_id_cd231362_fk_core_aten" FOREIGN KEY ("tipoAtendimento_id") REFERENCES public.core_atendimentosdepartamento(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.core_atendimento DROP CONSTRAINT "core_atendimento_tipoAtendimento_id_cd231362_fk_core_aten";
       public          postgres    false    3047    218    220            i           2606    27444 X   core_atendimentosdepartamento core_atendimentosdep_departamento_id_712e5126_fk_core_depa    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendimentosdepartamento
    ADD CONSTRAINT core_atendimentosdep_departamento_id_712e5126_fk_core_depa FOREIGN KEY (departamento_id) REFERENCES public.core_departamento(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_atendimentosdepartamento DROP CONSTRAINT core_atendimentosdep_departamento_id_712e5126_fk_core_depa;
       public          postgres    false    220    224    3054            j           2606    27454 \   core_atendimentosdepartamento core_atendimentosdep_tipo_atendimento_id_0d866dd2_fk_core_tipo    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_atendimentosdepartamento
    ADD CONSTRAINT core_atendimentosdep_tipo_atendimento_id_0d866dd2_fk_core_tipo FOREIGN KEY (tipo_atendimento_id) REFERENCES public.core_tipoatendimento(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_atendimentosdepartamento DROP CONSTRAINT core_atendimentosdep_tipo_atendimento_id_0d866dd2_fk_core_tipo;
       public          postgres    false    220    246    3103            �           2606    27655 =   core_cliente core_cliente_perfil_id_1c9cc5bf_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_cliente
    ADD CONSTRAINT core_cliente_perfil_id_1c9cc5bf_fk_auth_group_id FOREIGN KEY (perfil_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 g   ALTER TABLE ONLY public.core_cliente DROP CONSTRAINT core_cliente_perfil_id_1c9cc5bf_fk_auth_group_id;
       public          postgres    false    3004    258    203            �           2606    27660 :   core_cliente core_cliente_user_id_d7896daf_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_cliente
    ADD CONSTRAINT core_cliente_user_id_d7896daf_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 d   ALTER TABLE ONLY public.core_cliente DROP CONSTRAINT core_cliente_user_id_d7896daf_fk_auth_user_id;
       public          postgres    false    258    3012    207            k           2606    27416 J   core_departamento core_departamento_empresa_id_b18cc9c8_fk_core_empresa_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_departamento
    ADD CONSTRAINT core_departamento_empresa_id_b18cc9c8_fk_core_empresa_id FOREIGN KEY (empresa_id) REFERENCES public.core_empresa(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.core_departamento DROP CONSTRAINT core_departamento_empresa_id_b18cc9c8_fk_core_empresa_id;
       public          postgres    false    224    3064    228            l           2606    27421 L   core_departamento core_departamento_endereco_id_30b5f269_fk_core_endereco_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_departamento
    ADD CONSTRAINT core_departamento_endereco_id_30b5f269_fk_core_endereco_id FOREIGN KEY (endereco_id) REFERENCES public.core_endereco(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.core_departamento DROP CONSTRAINT core_departamento_endereco_id_30b5f269_fk_core_endereco_id;
       public          postgres    false    3072    232    224            o           2606    27505 X   core_departamentoprofissional core_departamentopro_departamento_id_d0d6a1db_fk_core_depa    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_departamentoprofissional
    ADD CONSTRAINT core_departamentopro_departamento_id_d0d6a1db_fk_core_depa FOREIGN KEY (departamento_id) REFERENCES public.core_departamento(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_departamentoprofissional DROP CONSTRAINT core_departamentopro_departamento_id_d0d6a1db_fk_core_depa;
       public          postgres    false    224    3054    226            m           2606    27401 X   core_departamentoprofissional core_departamentopro_profissional_id_b11f772e_fk_core_prof    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_departamentoprofissional
    ADD CONSTRAINT core_departamentopro_profissional_id_b11f772e_fk_core_prof FOREIGN KEY (profissional_id) REFERENCES public.core_profissional(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_departamentoprofissional DROP CONSTRAINT core_departamentopro_profissional_id_b11f772e_fk_core_prof;
       public          postgres    false    226    252    3121            n           2606    27407 ]   core_departamentoprofissional core_departamentopro_tipo_profissional_id_8dc7c694_fk_core_tipo    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_departamentoprofissional
    ADD CONSTRAINT core_departamentopro_tipo_profissional_id_8dc7c694_fk_core_tipo FOREIGN KEY (tipo_profissional_id) REFERENCES public.core_tipoprofissional(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_departamentoprofissional DROP CONSTRAINT core_departamentopro_tipo_profissional_id_8dc7c694_fk_core_tipo;
       public          postgres    false    226    3101    244            q           2606    27519 V   core_empresa_convenios core_empresa_convenios_convenio_id_eadb805d_fk_core_convenio_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_empresa_convenios
    ADD CONSTRAINT core_empresa_convenios_convenio_id_eadb805d_fk_core_convenio_id FOREIGN KEY (convenio_id) REFERENCES public.core_convenio(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_empresa_convenios DROP CONSTRAINT core_empresa_convenios_convenio_id_eadb805d_fk_core_convenio_id;
       public          postgres    false    222    230    3050            p           2606    27514 T   core_empresa_convenios core_empresa_convenios_empresa_id_429984f9_fk_core_empresa_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_empresa_convenios
    ADD CONSTRAINT core_empresa_convenios_empresa_id_429984f9_fk_core_empresa_id FOREIGN KEY (empresa_id) REFERENCES public.core_empresa(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.core_empresa_convenios DROP CONSTRAINT core_empresa_convenios_empresa_id_429984f9_fk_core_empresa_id;
       public          postgres    false    228    3064    230            r           2606    27526 B   core_escala core_escala_departamentoProfissi_baa53877_fk_core_depa    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_escala
    ADD CONSTRAINT "core_escala_departamentoProfissi_baa53877_fk_core_depa" FOREIGN KEY ("departamentoProfissional_id") REFERENCES public.core_departamentoprofissional(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.core_escala DROP CONSTRAINT "core_escala_departamentoProfissi_baa53877_fk_core_depa";
       public          postgres    false    234    3057    226            �           2606    27645 N   core_escalaintervalo core_escalaintervalo_escala_id_dc032186_fk_core_escala_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_escalaintervalo
    ADD CONSTRAINT core_escalaintervalo_escala_id_dc032186_fk_core_escala_id FOREIGN KEY (escala_id) REFERENCES public.core_escala(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.core_escalaintervalo DROP CONSTRAINT core_escalaintervalo_escala_id_dc032186_fk_core_escala_id;
       public          postgres    false    234    256    3075            s           2606    27532 L   core_paciente core_paciente_departamento_id_982e887a_fk_core_departamento_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_paciente
    ADD CONSTRAINT core_paciente_departamento_id_982e887a_fk_core_departamento_id FOREIGN KEY (departamento_id) REFERENCES public.core_departamento(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.core_paciente DROP CONSTRAINT core_paciente_departamento_id_982e887a_fk_core_departamento_id;
       public          postgres    false    238    224    3054            t           2606    27537 D   core_paciente core_paciente_endereco_id_20370ab8_fk_core_endereco_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_paciente
    ADD CONSTRAINT core_paciente_endereco_id_20370ab8_fk_core_endereco_id FOREIGN KEY (endereco_id) REFERENCES public.core_endereco(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.core_paciente DROP CONSTRAINT core_paciente_endereco_id_20370ab8_fk_core_endereco_id;
       public          postgres    false    232    3072    238            u           2606    27544 e   core_pacientedepartamentoprofissional core_pacientedeparta_departamentoProfissi_94d9e572_fk_core_depa    FK CONSTRAINT       ALTER TABLE ONLY public.core_pacientedepartamentoprofissional
    ADD CONSTRAINT "core_pacientedeparta_departamentoProfissi_94d9e572_fk_core_depa" FOREIGN KEY ("departamentoProfissional_id") REFERENCES public.core_departamentoprofissional(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_pacientedepartamentoprofissional DROP CONSTRAINT "core_pacientedeparta_departamentoProfissi_94d9e572_fk_core_depa";
       public          postgres    false    240    3057    226            v           2606    27549 \   core_pacientedepartamentoprofissional core_pacientedeparta_paciente_id_f0753164_fk_core_paci    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_pacientedepartamentoprofissional
    ADD CONSTRAINT core_pacientedeparta_paciente_id_f0753164_fk_core_paci FOREIGN KEY (paciente_id) REFERENCES public.core_paciente(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_pacientedepartamentoprofissional DROP CONSTRAINT core_pacientedeparta_paciente_id_f0753164_fk_core_paci;
       public          postgres    false    238    240    3081            �           2606    27618 G   core_profissional core_profissional_perfil_id_be73e1c3_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_profissional
    ADD CONSTRAINT core_profissional_perfil_id_be73e1c3_fk_auth_group_id FOREIGN KEY (perfil_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.core_profissional DROP CONSTRAINT core_profissional_perfil_id_be73e1c3_fk_auth_group_id;
       public          postgres    false    203    252    3004            �           2606    27638 c   core_profissional_tiposAtendimentos core_profissional_ti_atendimentosdepartam_9f600534_fk_core_aten    FK CONSTRAINT       ALTER TABLE ONLY public."core_profissional_tiposAtendimentos"
    ADD CONSTRAINT core_profissional_ti_atendimentosdepartam_9f600534_fk_core_aten FOREIGN KEY (atendimentosdepartamento_id) REFERENCES public.core_atendimentosdepartamento(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos" DROP CONSTRAINT core_profissional_ti_atendimentosdepartam_9f600534_fk_core_aten;
       public          postgres    false    3047    254    220            �           2606    27633 ^   core_profissional_tiposAtendimentos core_profissional_ti_profissional_id_ff4fe485_fk_core_prof    FK CONSTRAINT     �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos"
    ADD CONSTRAINT core_profissional_ti_profissional_id_ff4fe485_fk_core_prof FOREIGN KEY (profissional_id) REFERENCES public.core_profissional(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."core_profissional_tiposAtendimentos" DROP CONSTRAINT core_profissional_ti_profissional_id_ff4fe485_fk_core_prof;
       public          postgres    false    3121    254    252            �           2606    27623 D   core_profissional core_profissional_user_id_95594b96_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_profissional
    ADD CONSTRAINT core_profissional_user_id_95594b96_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.core_profissional DROP CONSTRAINT core_profissional_user_id_95594b96_fk_auth_user_id;
       public          postgres    false    207    252    3012                       2606    27607 N   core_prontuario core_prontuario_atendimento_id_ae53c0ad_fk_core_atendimento_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_prontuario
    ADD CONSTRAINT core_prontuario_atendimento_id_ae53c0ad_fk_core_atendimento_id FOREIGN KEY (atendimento_id) REFERENCES public.core_atendimento(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.core_prontuario DROP CONSTRAINT core_prontuario_atendimento_id_ae53c0ad_fk_core_atendimento_id;
       public          postgres    false    218    3043    250            �           2606    27612 J   core_prontuario core_prontuario_departamento_profiss_46b458ef_fk_core_paci    FK CONSTRAINT       ALTER TABLE ONLY public.core_prontuario
    ADD CONSTRAINT core_prontuario_departamento_profiss_46b458ef_fk_core_paci FOREIGN KEY (departamento_profissional_paciente_id) REFERENCES public.core_pacientedepartamentoprofissional(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.core_prontuario DROP CONSTRAINT core_prontuario_departamento_profiss_46b458ef_fk_core_paci;
       public          postgres    false    250    240    3085            ~           2606    27600 b   core_tipoatendimento_areaAtendimento core_tipoatendimento_areaatendimento_id_3bca587d_fk_core_area    FK CONSTRAINT     �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento"
    ADD CONSTRAINT core_tipoatendimento_areaatendimento_id_3bca587d_fk_core_area FOREIGN KEY (areaatendimento_id) REFERENCES public.core_areaatendimento(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento" DROP CONSTRAINT core_tipoatendimento_areaatendimento_id_3bca587d_fk_core_area;
       public          postgres    false    216    248    3038            |           2606    27587 T   core_tipoatendimento core_tipoatendimento_tipo_profissional_id_b1e19a65_fk_core_tipo    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_tipoatendimento
    ADD CONSTRAINT core_tipoatendimento_tipo_profissional_id_b1e19a65_fk_core_tipo FOREIGN KEY (tipo_profissional_id) REFERENCES public.core_tipoprofissional(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.core_tipoatendimento DROP CONSTRAINT core_tipoatendimento_tipo_profissional_id_b1e19a65_fk_core_tipo;
       public          postgres    false    246    3101    244            }           2606    27595 b   core_tipoatendimento_areaAtendimento core_tipoatendimento_tipoatendimento_id_e3b147b0_fk_core_tipo    FK CONSTRAINT     �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento"
    ADD CONSTRAINT core_tipoatendimento_tipoatendimento_id_e3b147b0_fk_core_tipo FOREIGN KEY (tipoatendimento_id) REFERENCES public.core_tipoatendimento(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."core_tipoatendimento_areaAtendimento" DROP CONSTRAINT core_tipoatendimento_tipoatendimento_id_e3b147b0_fk_core_tipo;
       public          postgres    false    3103    246    248            {           2606    27581 S   core_tipoprofissional core_tipoprofissiona_areaAtendimento_id_45687893_fk_core_area    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_tipoprofissional
    ADD CONSTRAINT "core_tipoprofissiona_areaAtendimento_id_45687893_fk_core_area" FOREIGN KEY ("areaAtendimento_id") REFERENCES public.core_areaatendimento(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.core_tipoprofissional DROP CONSTRAINT "core_tipoprofissiona_areaAtendimento_id_45687893_fk_core_area";
       public          postgres    false    244    3038    216            w           2606    27556 G   core_userprofile core_userprofile_departamento_id_14963af2_fk_core_depa    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_departamento_id_14963af2_fk_core_depa FOREIGN KEY (departamento_id) REFERENCES public.core_departamento(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_departamento_id_14963af2_fk_core_depa;
       public          postgres    false    242    3054    224            x           2606    27561 H   core_userprofile core_userprofile_empresa_id_c5a8b4b9_fk_core_empresa_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_empresa_id_c5a8b4b9_fk_core_empresa_id FOREIGN KEY (empresa_id) REFERENCES public.core_empresa(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_empresa_id_c5a8b4b9_fk_core_empresa_id;
       public          postgres    false    242    228    3064            y           2606    27566 E   core_userprofile core_userprofile_perfil_id_8ac5d178_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_perfil_id_8ac5d178_fk_auth_group_id FOREIGN KEY (perfil_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_perfil_id_8ac5d178_fk_auth_group_id;
       public          postgres    false    3004    203    242            z           2606    27571 B   core_userprofile core_userprofile_user_id_5141ad90_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_userprofile
    ADD CONSTRAINT core_userprofile_user_id_5141ad90_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.core_userprofile DROP CONSTRAINT core_userprofile_user_id_5141ad90_fk_auth_user_id;
       public          postgres    false    3012    242    207            b           2606    27163 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    2994    199    213            c           2606    27168 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    207    213    3012               I   x�3�(�O�,.���K��2�tL����,.)JL�/�2�t,I�KI�+I�2�t����9�S�R�3�jb���� rk         �   x�%���0B��0=$;ޥ��Q�~��%�x"�d�H�E=�=��c�V�V"����Ep B�@�A�Fg\�θ��q1�p37����	��G�p�4t���=��O�@-�Pп9!7�@|ҷ����4�Sݬmh�t�^%�O!}+���������GK������V8c      	   >  x����n�6������ɇK#Q�c8�^-P�6��؆�]��}��X)rș!� @���7�?�Cr3qۜ��pH��1��k�SdB��M��?�\#���(e!Xh� ;y�y�`���V�Ű�B�Sv��[;��$r-$3*�����s��� ����H��pK��؟�/����IvC������j��$G)�*�u����0��d%�>�����_ >n�~^�O��s����tUUK�?/RTZ<�$ق
�`��%�������h-���S=HSՙ����wd@���jG�9��u��*��J��ο7]��77�I?'�.g�>f�Y�\���/�$��řED�C^�ʓX茮��I�b߃t@�C,!����!��X��K�[5.fQ�1�X�j���R(t�jW���K��[?֛�'�Ǩ��eӨ�{h���='�Q,
$��O�@��,��ba:� �p��0�Y̓m.�g��x���<�(�lS�ީ���j������b8�K�_f6�Rl�0Eo��D��������Ɉ�O�7:��i�ެUPa���<��bƦ�{ ��)��Hbs�����e6F�I�|�㠔G��G�bAz��k�Ʈ@���g�ajӉ�
R���Oǉ�ȇb��ӡ"ɳ�f��|:P0+|�.��vW?�Df6p�v���$3�U�:�u�A&�#]�PZ�c�{(gջ��U���l${�?'3�g�9�9��V�C��h:][?߮Tf'�þ�d���Us+RVPĩ�=@�K����(2�+w͵;�9s&"��s#R��q 2��n��]+{�"7{�ٷj�d�LE1{�p$�%�5Òb	ʙK��p��g�(Ϙ�I-�K�6������Y_ۛ�鱉�62���q���ϯ���[��ݥ4کZ0�\��<LXr�r,11!�e�q�4�ގ;w��=��~~^?mV"7������=jO�A4?�OD�spM����tDA���r_���ҥL�s�2�q4���F�bYGG ��fa��x�>�&]i��y�Ua65O��{ӫϒw&�Z��w'F["����`c+�fT/)��*��f7�'��(���r��iH�Գ �����>���e�Mw���a!�vP��C,���4�t�X�ii9�?�^c� ���4�+B�S���A{hw =�#f��B�k{j�7-���IoR 3�2�ޔ &Fe(ބ ����5����}��㿶��GpP�p����RѪ6f6B�IQ�hpGw:���ۈg�6��pP8��T.��q�F_m� >���-�6�pH�Ŏc�b��j#,}��J���7�r�dւ��E��)+�X��n"�;>��Yګ��V�<�h�Fa��>�U-����Wׂ�Շ��E��>�j[����nV7�y}������
����^���1�C��Au=尺"�-��"�ղd�D�X�֭|H�Y'�!�y/��
�(W����}H'g�M�����L]4^ Y3�L<��Mjr������r.�C���iO�KUzz!Pl|1�6�\Z�[9A _4�M��I��*Y8��;U��Iu�<�Po���)�`l�.U9i?�}��/I��a�Z�         �   x�U�M�0 ����):x��ܦ��"�r*�Xn��2Tz��	�z.��Ï�ǹ�=�WCc��=+Z-)��:[��.9��U�^e\�E�)���b��s�ذ�L�G�FOO�J�@��D�!�` �������7�������4�@2�����#�~PS.u            x������ � �            x������ � �            x������ � �           x�USK��0\�O�	��|�=��Y261�r�Q�iV9�/����A����]�ГG#*�%��5T��(��RE��q�a�($�!���0���h m���
}��(��td�?qR�A/���b1�?N���N�iR.>�(O�+pDO����i
��eV���*3β����
EYg~�V�G�����߻�Mf���{��n�d�&�,��W���'2z��{2�Z�n�:��)�����޷z��<�qA�4��wd�MR�Fm�
�֕\֬��1h����܁��0�y�7�1,��v������7t�����M���c�ڔ�ӷR�C|��L9Όn�%Q��+��;�&E]};�)|t�3_g���y�6�����kZ|S�	���񹤪n�H�씎�3k�G�r��~�]}�";+C���
��m�����k}�@��J�eY��Î*p]@3l���ȴ�-3BJ`{n���G3���/���o��,�d�����~9T��#�R��y����=�9�8�_�ڔ�q���jE[|�<��H������?��*�      D      x������ � �            x������ � �            x������ � �      B      x������ � �            x������ � �             x������ � �      "      x������ � �      $      x������ � �      &      x������ � �      (      x������ � �      *      x������ � �      @      x������ � �      ,      x������ � �      .      x������ � �      0      x������ � �      <      x������ � �      >      x������ � �      :      x������ � �      6      x������ � �      8      x������ � �      4      x������ � �      2      x������ � �         �  x���Ko�H��ί������A�	)Z���K���N,����d��L���搱���Q�UyT���/�~��Na@J	p�}!e��-�N���������t�v���w7�٫s}������u۔m��O?�eU��>�~��������OP�0��n%��c�i�)Wk�8���˹�͒�b�' �Rf`j�����/�s9lv�K)�H m\�������ʹ��)���BJ#S/g����|w��e��m�>���}�Y��7����u)S{��f	"W@�ӗ��l��>�J[0*�i9�}sυSՏi��d� BN.t���lX��#8̭@MW`�$�h��q[�u]5���D]&(l.�ǝoWW�����g���c�m�W���� ���a����D`&��&a���6�婉�l�W��b�+x����Db6�d�XU�Qbyj�1�;��ޯ#�ˣ�� � c5�;~�Ȳ+Љ�\P ,H�J�0Y~	��\ �{T�w�V�}�/B��@�?Gv<���`�������1׶I,�L�{cK��hl�n�6ї�
d*�[�m�� w� �GM"��&�p�uw[�8-�?ї���8=��
��̐�
#����b�
����w+Rz�0f+#P�=ǔ�؏�}Su1�3L�.(�*\��w��[9^z;�c����9p��nuj+R}���'\�Bp��n��X���Nm�X~;��c=���H�t�|�-���rB{�9M+����a*.���jHƗ8Z!.���Su1�� e��+��G}(ϧY�TW��^$=��zi��.|�,ݿ��Aw�BY��>��^X�~˺x�(����8���J�!Iu�k�Mwn����b�0�S\�J��d�Y���6� �$x������_w�x�.�H
��/����P�g�K�������F0:݈��~+�_c����>T��i���v����[����+2c�>3������F�?           x�u��N�0���A$���]��iM�H��I'���&�l7U����Z�X�\��g��(\�ċM��Bfk��k"����R��H��W������A�.��{��N5�N{�>ɫ��{9|m��e �B&D�;�E�к��&����Pb�B�
�
�U�,�^VG�/Z"SB�C��DL�t8U�Ft�?��av~S-E��&0��;�T�?�eO8)����w��h�d�=��"�L�����5ae/��q57������N^� ��D��           x���ێ�0@��W����3��[*Yn�VScV���1Y'�%/s�93ch�aHnH�<��!���O�v$o�o@~ 8;��-�ҟ�찱sz�8�A{���B� Z�®!h���D��Dׇg������6C2����W�2r�����`�t�5������&K�Z��f����0�3��m��TP*�U�%��b�i�h�7��4����*?S�d�*�^P�/���{J J/])얲\J:aL�v	+��T�EtvJ�x����#*�K5 �"�����n�ng�J4/�	�锗T>l�O6�8�޻C4��&�>h;R�)/8ZqjS�3�LJ�&�*Is��s ���
���0��aRU(�R��c6�����f�َ,�u�S��^�n��\����p]i$� @f��M�d�}���ܖ
�2�JS��m��y�ye�(�"4m~��N�S��R��"���^V�Hk��Qt6wi8�>�D0�M���ad"�@9�2+�*�����: ��ݿ����?W��      E   =  x���n�@F���7���;IW"#C4�ˤ�9�Z�ry��I�ݟ���1��:}(��ԋl,U}l��i� �lỴ&��A�OA썤΁ڔ����*��f�Ne�ި>;-���'LV$�K"G3M��1��{������UEBD.L�Ƥ���x��S�ʲ���Zr�·�{�4��q��q���"�lY
��������9&�!�`,��k3m��a.���$di��B�h�؇�u��3i#ؤ���c���7�X�a)�
4ME�;B���su+��[��ko�EޛC9�����v������lj��g���$I?	(��     