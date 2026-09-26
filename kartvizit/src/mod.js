// ?mod=mockup veya ?katman=folyo|kabartma|beyaz|murekkep → <html data-*>
(function(){var q=new URLSearchParams(location.search),h=document.documentElement;
q.get('mod')&&(h.dataset.mod=q.get('mod'));q.get('katman')&&(h.dataset.katman=q.get('katman'));})();
