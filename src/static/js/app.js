document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.getElementById("menu-toggle");
    const mainNav = document.getElementById("main-nav");
    const menuClose = document.getElementById("menu-close");
    const langToggle = document.getElementById("lang-toggle");
    const viewToggle = document.getElementById("view-toggle");
    const messages = {
        "Veuillez remplir tous les champs du formulaire de contact.": "Please complete every contact form field.",
        "Veuillez saisir une adresse email valide.": "Please enter a valid email address.",
        "Le formulaire n'est pas relié à une messagerie. Utilisez l'adresse email affichée ci-dessous.": "This form is not connected to an email service. Use the email address shown below.",
        "Tous les champs obligatoires doivent être remplis.": "Please complete all required fields.",
        "L'adresse email est invalide.": "The email address is invalid.",
        "Le mot de passe doit contenir au moins 4 caractères.": "The password must contain at least 4 characters.",
        "Le budget mensuel ne peut pas être négatif.": "The monthly budget cannot be negative.",
        "Le budget mensuel doit être un nombre valide.": "Enter a valid monthly budget.",
        "Cet email est déjà utilisé par un autre compte.": "This email is already registered.",
        "Compte créé avec succès ! Vous pouvez vous connecter.": "Account created. You can now log in.",
        "Email ou mot de passe incorrect.": "Incorrect email or password.",
        "Connexion réussie.": "You are now logged in.",
        "Vous avez été déconnecté.": "You have been logged out.",
        "Veuillez vous connecter pour accéder à cette page.": "Please log in to access this page.",
        "Tous les champs de la dépense sont obligatoires.": "Please complete every expense field.",
        "La description ne doit pas dépasser 150 caractères.": "The description must be 150 characters or fewer.",
        "Le montant doit être un nombre supérieur à 0.": "Enter an amount greater than zero.",
        "La date saisie est invalide.": "The date is invalid.",
        "La catégorie sélectionnée est invalide.": "The selected category is invalid.",
        "Dépense introuvable ou accès non autorisé.": "Expense not found or access denied.",
        "Dépense ajoutée avec succès.": "Expense added.",
        "Dépense modifiée avec succès.": "Expense updated.",
        "Dépense supprimée.": "Expense deleted.",
        "Impossible de supprimer cette dépense.": "Could not delete this expense.",
        "Saisissez un budget valide supérieur ou égal à zéro.": "Enter a valid budget of zero or more.",
        "Budget mensuel mis à jour.": "Monthly budget updated."
    };

    if (menuToggle && mainNav) {
        menuToggle.addEventListener("click", () => {
            const isOpen = mainNav.classList.toggle("is-open");
            menuToggle.setAttribute("aria-expanded", String(isOpen));
        });
    }
    if (menuClose && menuToggle && mainNav) {
        menuClose.addEventListener("click", () => {
            mainNav.classList.remove("is-open");
            menuToggle.setAttribute("aria-expanded", "false");
        });
    }

    /** Apply the selected interface language to text, placeholders, and alerts. */
    function applyLanguage(lang) {
        document.documentElement.lang = lang;
        localStorage.setItem("expense_tracker_lang", lang);
        if (langToggle) langToggle.textContent = lang === "fr" ? "EN" : "FR";
        document.querySelectorAll("[data-fr][data-en]").forEach((el) => {
            const value = el.getAttribute(lang === "en" ? "data-en" : "data-fr");
            if (value !== null) el.textContent = value;
        });
        document.querySelectorAll("[data-placeholder-fr][data-placeholder-en]").forEach((el) => {
            el.placeholder = el.getAttribute(lang === "en" ? "data-placeholder-en" : "data-placeholder-fr");
        });
        document.querySelectorAll("[data-category-fr][data-category-en]").forEach((el) => {
            el.textContent = el.getAttribute(lang === "en" ? "data-category-en" : "data-category-fr");
        });
        document.querySelectorAll("[data-aria-fr][data-aria-en]").forEach((el) => {
            el.setAttribute("aria-label", el.getAttribute(lang === "en" ? "data-aria-en" : "data-aria-fr"));
        });
        document.querySelectorAll(".flash-alert span").forEach((el) => {
            const original = el.getAttribute("data-original-message") || el.textContent.trim();
            el.setAttribute("data-original-message", original);
            el.textContent = lang === "en" ? (messages[original] || original) : original;
        });
        updateViewToggleLabel();
    }

    /** Update the view switch label to describe the layout available after a click. */
    function updateViewToggleLabel() {
        if (!viewToggle) return;
        const lang = localStorage.getItem("expense_tracker_lang") || "fr";
        const mobile = document.body.classList.contains("force-mobile");
        viewToggle.textContent = mobile ? (lang === "en" ? "Desktop" : "Bureau") : "Mobile";
        viewToggle.setAttribute("aria-label", mobile
            ? (lang === "en" ? "Switch to desktop layout" : "Passer à la vue bureau")
            : (lang === "en" ? "Switch to mobile layout" : "Passer à la vue mobile"));
    }

    /** Apply and persist the requested mobile or desktop layout mode. */
    function applyViewMode(mode) {
        document.body.classList.remove("force-mobile", "force-desktop");
        if (mode === "mobile") document.body.classList.add("force-mobile");
        if (mode === "desktop") document.body.classList.add("force-desktop");
        localStorage.setItem("expense_tracker_view", mode);
        updateViewToggleLabel();
    }

    if (langToggle) langToggle.addEventListener("click", () => {
        const current = localStorage.getItem("expense_tracker_lang") || "fr";
        applyLanguage(current === "fr" ? "en" : "fr");
    });
    if (viewToggle) viewToggle.addEventListener("click", () => {
        const mobile = document.body.classList.contains("force-mobile");
        applyViewMode(mobile ? "desktop" : "mobile");
    });

    applyViewMode(localStorage.getItem("expense_tracker_view") || "desktop");
    applyLanguage(localStorage.getItem("expense_tracker_lang") || "fr");

    document.querySelectorAll("[data-password-toggle]").forEach((button) => {
        const input = document.getElementById(button.dataset.passwordToggle);
        if (!input) return;
        button.addEventListener("click", () => {
            const showing = input.type === "text";
            input.type = showing ? "password" : "text";
            const lang = localStorage.getItem("expense_tracker_lang") || "fr";
            button.setAttribute("aria-label", showing
                ? (lang === "en" ? "Show password" : "Afficher le mot de passe")
                : (lang === "en" ? "Hide password" : "Masquer le mot de passe"));
        });
    });

    document.querySelectorAll(".flash-alert").forEach((alert) => {
        /** Animate and remove a temporary notification. */
        const closeAlert = () => {
            alert.classList.add("is-hiding");
            window.setTimeout(() => alert.remove(), 200);
        };
        alert.querySelector(".flash-close")?.addEventListener("click", closeAlert);
        window.setTimeout(closeAlert, 5000);
    });

    const histogram = document.querySelector("[data-histogram-columns]");
    const histogramSlider = document.querySelector("[data-histogram-slider]");
    if (histogram && histogramSlider) {
        const columns = Array.from(histogram.querySelectorAll(".histogram-column"));
        const startLabel = document.querySelector("[data-histogram-start]");
        const endLabel = document.querySelector("[data-histogram-end]");
        let histogramInitialized = false;
        /** Refresh the visible monthly bars for the current screen width and slider value. */
        const refreshHistogram = () => {
            const visibleMonths = window.matchMedia("(max-width: 767px)").matches ? 5 : 10;
            const maximumStart = Math.max(0, columns.length - visibleMonths);
            histogramSlider.max = String(maximumStart);
            if (!histogramInitialized) {
                histogramSlider.value = String(maximumStart);
                histogramInitialized = true;
            }
            if (Number(histogramSlider.value) > maximumStart) histogramSlider.value = String(maximumStart);
            const start = Number(histogramSlider.value);
            columns.forEach((column, index) => { column.hidden = index < start || index >= start + visibleMonths; });
            if (startLabel) startLabel.textContent = columns[start].querySelector(".histogram-label").textContent;
            if (endLabel) endLabel.textContent = columns[start + visibleMonths - 1].querySelector(".histogram-label").textContent;
        };
        histogramSlider.addEventListener("input", refreshHistogram);
        window.addEventListener("resize", refreshHistogram);
        refreshHistogram();
    }

    const dynamicFilterForm = document.querySelector("[data-dynamic-filters]");
    if (dynamicFilterForm) {
        const searchInput = dynamicFilterForm.querySelector("[name='q']");
        const categoryInput = dynamicFilterForm.querySelector("[data-filter-category]");
        const monthInput = dynamicFilterForm.querySelector("[data-filter-month]");
        const rows = Array.from(document.querySelectorAll("[data-expense-row]"));
        const count = document.querySelector("[data-filter-count]");
        const emptyState = document.querySelector("[data-filter-empty]");
        const pagination = document.querySelector("[data-pagination]");
        const previousPage = document.querySelector("[data-page-previous]");
        const nextPage = document.querySelector("[data-page-next]");
        const pageStatus = document.querySelector("[data-page-status]");
        const pageSize = 10;
        let currentPage = 0;
        /** Filter expense rows and display the matching pagination page. */
        const applyFilters = () => {
            const query = (searchInput?.value || "").trim().toLocaleLowerCase();
            const category = categoryInput?.value || "";
            const monthValue = (monthInput?.value || "").trim();
            const monthMatch = monthValue.match(/^(0[1-9]|1[0-2])\/(\d{4})$/);
            const month = monthMatch ? `${monthMatch[2]}-${monthMatch[1]}` : "";
            const matchingRows = rows.filter((row) => {
                const matches = (!query || row.textContent.toLocaleLowerCase().includes(query))
                    && (!category || row.dataset.categoryId === category)
                    && (!month || row.dataset.expenseDate.startsWith(month));
                return matches;
            });
            const pageCount = Math.max(1, Math.ceil(matchingRows.length / pageSize));
            currentPage = Math.min(currentPage, pageCount - 1);
            const firstRow = currentPage * pageSize;
            rows.forEach((row) => {
                const matchingIndex = matchingRows.indexOf(row);
                row.hidden = matchingIndex < firstRow || matchingIndex >= firstRow + pageSize;
            });
            if (count) count.textContent = String(matchingRows.length);
            if (emptyState) emptyState.hidden = matchingRows.length !== 0;
            if (pagination) pagination.hidden = matchingRows.length <= pageSize;
            if (previousPage) previousPage.disabled = currentPage === 0;
            if (nextPage) nextPage.disabled = currentPage >= pageCount - 1;
            if (pageStatus) pageStatus.textContent = `Page ${currentPage + 1} / ${pageCount}`;
        };
        /** Return to the first page after a filter value changes. */
        const resetPagination = () => { currentPage = 0; applyFilters(); };
        dynamicFilterForm.addEventListener("submit", (event) => event.preventDefault());
        searchInput?.addEventListener("input", resetPagination);
        categoryInput?.addEventListener("change", resetPagination);
        monthInput?.addEventListener("change", resetPagination);
        monthInput?.addEventListener("input", resetPagination);
        dynamicFilterForm.querySelector("[data-clear-filters]")?.addEventListener("click", () => {
            if (searchInput) searchInput.value = "";
            if (categoryInput) categoryInput.value = "";
            if (monthInput) monthInput.value = "";
            resetPagination();
        });
        previousPage?.addEventListener("click", () => { currentPage -= 1; applyFilters(); });
        nextPage?.addEventListener("click", () => { currentPage += 1; applyFilters(); });
        applyFilters();
    }

    document.querySelectorAll(".delete-expense-form").forEach((form) => {
        form.addEventListener("submit", (event) => {
            const lang = localStorage.getItem("expense_tracker_lang") || "fr";
            const message = lang === "en"
                ? "Are you sure you want to delete this expense?"
                : "Voulez-vous vraiment supprimer cette dépense ?";
            if (!window.confirm(message)) event.preventDefault();
        });
    });
});
