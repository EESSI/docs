# Overview of adding software to EESSI

We welcome contributions to the EESSI software stack. This page shows the procedure and provides links to the contribution policy and the technical details of making a contribution. 

## Contribute a software to the EESSI software stack

<pre class="mermaid">
%%{init: { 'theme':'forest', 'sequence': {'useMaxWidth':false} } }%%
flowchart TB
    I(contributor)  
    K(reviewer)
    A(Is there an EasyConfig for software) -->|No|B(Create an EasyConfig and contribute it to EasyBuild)
    A --> |Yes|D(Create a PR to software-layer)
    B --> C(Evaluate and merge pull request)
    C --> D
    D --> E(Review PR & trigger builds)
    E --> F(Debug build issue if needed)
    F --> G(Deploy tarballs to S3 bucket)
    G --> H(Ingest tarballs in EESSI by merging staging PRs)
     classDef blue fill:#9abcff,stroke:#333,stroke-width:2px;
     class A,B,D,F,I blue
</pre>


## Contributing a ReFrame test to the EESSI test suite

Ideally, a contributor prepares a ReFrame test for the software to be added to the EESSI software stack. 

<pre class="mermaid">
%%{init: { 'theme':'forest', 'sequence': {'useMaxWidth':false} } }%%
flowchart TB

    Z(Creat ReFrame test & PR to tests-suite) --> Y(Review PR & run new test)
    Y --> W(Debug issue if needed) 
    W --> V(Review PR if needed)
    V --> U(Merge PR)
     classDef blue fill:#9abcff,stroke:#333,stroke-width:2px;
     class Z,W blue
</pre>
</div>


# More about adding software to EESSI

* [Contribution policy](contribution_policy.md)
* [Opening a pull request *(for contributors)*](opening_pr.md)
* [Building software *(for maintainers)*](building_software.md)
* [Debugging failed builds *(for contributors + maintainers)*](debugging_failed_builds.md)
* [Deploying software *(for maintainers)*](deploying_software.md)

If you need help with adding software to EESSI, please [open a support request](../support.md).
