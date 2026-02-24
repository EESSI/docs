{% set data = load_json_eessi_software() %}
{% set software = data.software %}

# Software available in EESSI

Overview of software available in [EESSI's production repository `software.eessi.io`](../repositories/software.eessi.io.md).

<em>{{ data.n_software }} unique software projects (+ {{ data.n_extensions }} unique extensions)</em>

<!-- see also docs/available_software/javascripts/software-filter.js -->
<input type="search" id="software-search" class="md-input"
       placeholder="Filter software..."
       style="width:100%; margin-bottom:1rem;">

<div class="grid cards" markdown>

{% for pkg in software %}
{% set pkg_slug = pkg.name | replace(' ', '-') %}
{% if pkg.is_extension -%}
- <span class="software-item software-card"
    data-search="name:{{ pkg.name }} extension ext_type:{{ pkg.type }}" >
    <span class="software-name"><a href="https://eessi.io/docs/available_software/detail/{{ pkg_slug }}">{{ pkg.name }}</a></span>
    <span class="software-more-info"><small>(extension)</small></span>
    <br/>
    <p class="software-description">
    {{ pkg.name }} is a {% if pkg.type == "python" -%} Python package{% elif pkg.type == "r" -%}R library{% elif pkg.type == "perl" -%}Perl module{% endif %}
    that is included as extension in the following software installations:
    <ul>
    {% for parent in pkg.all_parent_names %}
    {% set parent_slug = parent | replace(' ', '-') %}
    <li><a href="https://eessi.io/docs/available_software/detail/{{ parent_slug }}">{{ parent }}</a></li>
    {% endfor %}
    </p>
    </ul>
  </span>
{% else -%}
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
    <span class="software-gpus">Supported GPU families: {% if pkg.gpu_families == '' -%}<em>(none)</em>{% else -%}{% if 'AMD' in pkg.gpu_families -%}<span class="software-gpu-amd">AMD</span>{% endif %}{% if 'NVIDIA' in pkg.gpu_families -%}<span class="software-gpu-nvidia">NVIDIA</span>{% endif %}{% endif %}</span>
    <br/>
  </span>
{% endif %}
{% endfor %}

</div>

---

<small><em>Last update: {{ data.timestamp }}</em></small>
