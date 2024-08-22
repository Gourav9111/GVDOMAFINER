#SUBDOMAIN FINDER BY GOURAV 
import dns.resolver
import pyfiglet

subdomains = [
    'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'secure',
    'server', 'ns1', 'ns2', 'autodiscover', 'blog', 'test', 'm',
    'shop', 'cpanel', 'whm', 'webdisk', 'ns', 'pop', 'imap', 'mobile',
    'forum', 'dev', 'beta', 'api', 'admin', 'cdn', 'img', 'static',
    'docs', 'support', 'portal', 'api', 'backup', 'mx', 'mail1', 'web',
    'lb', 'prod', 'app', 'dns', 'stage', 'vpn', 'mx1', 'dev', 'chat', 'webapi', 'api-v1', 'api-v2', 'api-v3', 'api-auth', 'auth-api',
    'api-login', 'login-api', 'database', 'db', 'db1', 'db2', 'db3',
    'db-server', 'db-admin', 'db-login', 'db-backup', 'mysql', 'mysql-db',
    'postgres', 'postgresql', 'mssql', 'sql', 'sqldb', 'mongodb',
    'oracle', 'oracledb', 'nosql', 'redis', 'db-master', 'db-slave',
    'db-replica', 'db-prod', 'db-test', 'database1', 'database2',
    'login-panel', 'user-login', 'admin-login', 'secure-login', 
    'portal-login', 'panel', 'control-panel', 'secure-panel', 
    'admin-panel', 'login-portal', 'admin-portal', 'secure-portal',
    'https', 'https-api', 'https-db', 'secure-db', 'ssl', 'ssl-api',
    'ssl-db', 'secure-site', 'secure-app', 'secure-server', 'ssl-panel',
    'api-secure', 'webapi-secure', 'data-api', 'api-data', 'data-backup',
    'data-storage', 'secure-storage', 'login-secure', 'login-ssl',
    'auth-secure', 'auth-ssl', 'ssl-login', 'api-ssl', 'backup-db',
    'backup-api', 'secure-auth', 'data-secure', 'data-ssl', 'api-storage',
    'secure-access', 'admin-secure', 'admin-ssl', 'user-secure',
    'user-ssl', 'panel-secure', 'panel-ssl', 'app-secure', 'app-ssl',
    'secure-db1', 'secure-db2', 'ssl-db1', 'ssl-db2', 'ssl-admin',
    'ssl-auth', 'ssl-gateway', 'https-admin', 'https-auth', 'https-user',
    'secure-https', 'db-https', 'db-secure-https', 'panel-https','www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'secure',
    'server', 'ns1', 'ns2', 'autodiscover', 'blog', 'test', 'm',
    'shop', 'cpanel', 'whm', 'webdisk', 'ns', 'pop', 'imap', 'mobile',
    'forum', 'dev', 'beta', 'api', 'admin', 'cdn', 'img', 'static',
    'docs', 'support', 'portal', 'api', 'backup', 'mx', 'mail1', 'web',
    'lb', 'prod', 'app', 'dns', 'stage', 'vpn', 'mx1', 'dev', 'chat',
    'office', 'files', 'video', 'media', 'news', 'cms', 'blog1',
    'webdev', 'monitor', 'api2', 'cache', 'staging', 'demo', 'cloud',
    'api-dev', 'docs1', 'img1', 'test1', 'test2', 'beta1', 'app1',
    'mail2', 'mail3', 'download', 'api3', 'auth', 'mailtest', 'sandbox',
    'monitoring', 'backup1', 'dns1', 'files1', 'config', 'api-test',
    'git', 'repo', 'mirror', 'user', 'payment', 'client', 'content',
    'login', 'static1', 'metrics', 'secure1', 'api-prod', 'api-backup',
    'cdn1', 'cdn2', 'sso', 'partner', 'gateway', 'health', 'track',
    'server1', 'node1', 'node2', 'node3', 'assets', 'images', 'events',
    'email', 'marketing', 'sys', 'connect', 'registry', 'internal',
    'identity', 'public', 'private', 'services', 'api4', 'test3',
    'backup2', 'vhost', 'proxy', 'auth1', 'login1', 'services1',
    'app2', 'm1', 'api5', 'test4', 'mail4', 'support1', 'portal1'
]

def resolve_subdomain(subdomain, domain, retries=3):
    for attempt in range(retries):
        try:
            full_domain = f"{subdomain}.{domain}"
            resolver = dns.resolver.Resolver()
            resolver.timeout = 10
            resolver.lifetime = 10
            answers = resolver.resolve(full_domain, 'A')
            return full_domain, answers[0].address
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
            return None
        except dns.resolver.LifetimeTimeout:
            print(f"Timeout occurred for {full_domain} on attempt {attempt + 1}")
    return None

def enumerate_subdomains(domain):
    print(f"Enumerating subdomains for {domain}...")
    found_subdomains = []
    for subdomain in subdomains:
        result = resolve_subdomain(subdomain, domain)
        if result:
            found_subdomains.append(result)
            print(f"Found: {result[0]} -> {result[1]}")
    return found_subdomains

if __name__ == "__main__":
    banner = pyfiglet.figlet_format("GVDOMAFINER")
    print(banner)
    domain = input("Enter the domain to enumerate subdomains: ")
    found_subdomains = enumerate_subdomains(domain)
    
    print("\nEnumeration complete.")
    if found_subdomains:
        print("\nFound subdomains:")
        for sub in found_subdomains:
            print(f"{sub[0]} -> {sub[1]}")
    else:
        print("No subdomains found.")
go