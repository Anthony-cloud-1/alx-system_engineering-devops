### Postmortem: Website Downtime Incident

#### Issue Summary
**Duration:** The outage lasted from 10:00 AM to 12:45 PM GMT on May 1, 2024.  
**Impact:** During this period, approximately 65% of users experienced slow loading times and intermittent accessibility issues with the main customer portal.  
**Root Cause:** The root cause was identified as a misconfigured load balancer, which led to uneven traffic distribution across our web servers.

#### Timeline
- **10:00 AM:** Issue detected when critical response time alerts were triggered from our monitoring system.
- **10:05 AM:** Initial investigation by on-duty system engineers suggested a spike in traffic, but further analysis indicated normal traffic levels.
- **10:30 AM:** Customer support reported multiple user complaints about website unavailability.
- **10:45 AM:** Traffic distribution and server health checks showed discrepancies; two out of five servers were handling 80% of the traffic.
- **11:00 AM:** Misleading path initially suspected a DDoS attack, but was ruled out by security team after reviewing firewall logs.
- **11:20 AM:** Incident escalated to network engineering team to review load balancer configurations.
- **12:00 PM:** Network team identified a configuration error in the load balancer that directed much of the traffic to fewer servers.
- **12:30 PM:** Configuration fix applied, and traffic began to distribute evenly across all servers.
- **12:45 PM:** System monitoring confirmed recovery, and functionality was fully restored.

#### Root Cause and Resolution
The main cause of the outage was a misconfiguration in the load balancer’s session persistence settings, which inadvertently directed a disproportionate amount of user traffic to just two of our servers, overwhelming them and leading to slow response times and partial outages. This was compounded by an automated script that incorrectly reassigned server weights in the load balancing pool.

The resolution involved correcting the load balancer settings to ensure even traffic distribution and disabling the problematic script until it could be reviewed and rewritten. The network team manually adjusted the server weights and restarted the load balancer to immediately mitigate the issue, followed by a system-wide review to confirm that all settings were restored to their correct parameters.

#### Corrective and Preventative Measures
To prevent future occurrences of this issue, the following measures have been proposed and are currently being implemented:
- **Review and Audit of Load Balancer Configurations:** All load balancer configurations will be audited by the network team to ensure they meet our standards and practices.
- **Update Monitoring and Alerts:** Enhance monitoring systems to include checks for uneven traffic distribution and add alerts for discrepancies in server load.
- **Automated Script Safeguards:** Introduce additional checks and balances in automated scripts that modify network configurations. Scripts will now require manual approval before changes go live.
- **Incident Response Training:** Conduct quarterly incident response drills for the engineering team to prepare for similar incidents.
- **Documentation Updates:** Update our internal documentation and training materials to include this incident as a case study for troubleshooting network and load balancing issues.

By implementing these corrective actions, we aim to improve our system’s resilience and reduce the likelihood of similar disruptions in the future, ensuring a reliable user experience across all our platforms.
