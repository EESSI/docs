{% set data = load_json_eessi_software() %}
{% set software = data.software %}
{% set extensions = data.extensions %}

# Software available in EESSI

<em>{{ data.n_software }} unique software projects are currently available in EESSI (+ {{ data.n_extensions }} unique extensions)</em>

<input type="search" id="software-search" class="md-input"
       placeholder="Filter software..."
       style="width:100%; margin-bottom:1rem;">

<div class="grid cards" markdown>

{% for pkg in software %}
{% set pkg_slug = pkg.name | replace(' ', '-') %}
- <span class="software-item software-card"
       data-search="name:{{ pkg.name }} {{ pkg.homepage }} {{ pkg.description }} {{ pkg.cpu_families }} {{ pkg.eessi_versions }} ">

    <span class="software-name"><a href="https://eessi.io/docs/available_software/detail/{{ pkg_slug }}">{{ pkg.name }}</a></span>
    <!-- <span class="software-versions">{% if pkg.n_versions == 1 -%}({{ pkg.n_versions }} version){% else -%}({{ pkg.n_versions }} versions){% endif %}</span> -->
    <span class="software-more-info"><a href="https://eessi.io/docs/available_software/detail/{{ pkg_slug }}">(more details)</a></span>
    <br/>
    <span class="software-link">{{ pkg.homepages }}</span>
    <br/>
    <p class="software-description">
    {{ pkg.description }}
    </p>
    <span class="software-eessi-versions">Available in EESSI versions: {% if '2023.06' in pkg.eessi_versions -%}<span class="software-eessi-version-202306">2023.06</span>{% endif %}{% if '2025.06' in pkg.eessi_versions -%}<span class="software-eessi-version-202506">2025.06</span>{% endif %}</span>
    <br/>
    <span class="software-cpus">Supported CPU families: {% if 'AMD' in pkg.cpu_families -%}<span class="software-cpu-amd">AMD</span>{% endif %}{% if 'Intel' in pkg.cpu_families -%}<span class="software-cpu-intel">Intel</span>{% endif %}{% if 'Arm' in pkg.cpu_families -%}<span class="software-cpu-arm">Arm</span>{% endif %}{% if 'RISC-V' in pkg.cpu_families -%}<span class="software-cpu-riscv">RISC-V</span>{% endif %}</span>
    <br/>
    <span class="software-gpus">Supported GPU families: <span class="software-gpu-amd">AMD</span> <span class="software-gpu-nvidia">NVIDIA</span></span>
    <br/>
  </span>
{% endfor %}

{% for ext in extensions.values() %}
{% set ext_slug = ext.name | replace(' ', '-') %}
- <span class="software-item software-card"
    data-search="name:{{ ext.name }} extension" >
    <span class="software-name"><a href="https://eessi.io/docs/available_software/detail/{{ ext_slug }}">{{ ext.name }}</a> <em>(extension)</em></span>
    <br/>
    <p class="software-description">
    {% if ext.type == "python" -%} Python package{% elif ext.type == "r" -%}R library{% elif ext.type == "perl" -%}Perl module{% endif %} included as extension to the following
    software installations:
    <ul>
    {% for parent in ext.parents %}
    {% set parent_slug = parent | replace(' ', '-') %}
    <li><a href="https://eessi.io/docs/available_software/detail/{{ parent_slug }}">{{ parent }}</a></li>
    {% endfor %}
    </p>
    </ul>
  </span>
{% endfor %}

</div>

<small><em>Last update: {{ data.timestamp }}</em></small>
