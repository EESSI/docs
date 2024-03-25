/**
 * Copyright 2023-2023 Ghent University
 *
 * This file is part of vsc_user_docs,
 * originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
 * with support of Ghent University (http://ugent.be/hpc),
 * the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
 * the Flemish Research Foundation (FWO) (http://www.fwo.be/en)
 * and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
 *
 * https://github.com/hpcugent/vsc_user_docs
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 * @author: Michiel Lachaert
 */

/**
 * A function that populates the table on the module overview page with information about all the available modules.
 */
function populate_overview(json_data) {
    fetch(json_data)
        .then((response) => response.json())
        .then((json) => {
            // Set generated time
            const p = document.getElementById("time")
            p.innerText = `This data was automatically generated ${json.time_generated}`


            // CONSTRUCT TABLE

            // list with all the names of the clusters
            const all_clusters = json.clusters.map(x => {
		    //Todo: split up the strings of the clusters to automate the hierarchy of the table header
		    console.log(x)
		    let pathArray = x.split("/")
		    pathArray = pathArray.slice(7)
		    console.log(pathArray)
		    console.log(pathArray[pathArray.length -1])
		    x = pathArray[pathArray.length -1]
		    //x = pathArray
                    return ({"title": x})
                })
	    console.log(all_clusters)
            console.log([...[{"title": "name"}], ...all_clusters])
            const table = new DataTable('#overview_table', {
		columns: [...[{"title": "name"}], ...all_clusters],
                paging: false,
                columnDefs: [
                    {
                        targets: "_all",
                        className: 'dt-body-center'
                    }
                ]
            });
            console.log(table)


            // ADD DATA
            let new_rows = [];

            // list_avaible contains a list with booleans.
            // These booleans indicates if the software is available on the corresponding cluster.
            for (const [software, list_available] of Object.entries(json.modules)) {
                let new_row = [`<a href="../detail/${software}">${software}</a>`];
                list_available.forEach(bool => new_row.push(bool ? "x" : "-"));
                new_rows.push(new_row);
            }

            table.rows.add(new_rows).draw();
        })
}

// Only start populating the table if the correct page has been loaded.
document$.subscribe(function() {
    if (document.getElementById("overview_table")) {
        populate_overview("../data/json_data.json")
    }
})
