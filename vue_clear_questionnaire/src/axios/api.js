import service from "./http";


const api = {
    test(data) {
        return service.post('user/tokenTest', data).then(res => res)
    },
    emailRegister(data) {
        return service.post('user/email/register', data).then(res => res)
    },
    emailActivate(data) {
        return service.post('user/email/activate', data).then(res => res)
    },
    emailForgot(data) {
        return service.post('user/email/forgot', data).then(res => res)
    },
    emailChange(data) {
        return service.post('user/email/change', data).then(res => res)
    },
    accountLogin(data) {
        return service.post('user/account/login', data).then(res => res)
    },
    getUserInfo() {
        return service.post('user/get/info').then(res => res)
    },
    changeUsername(data) {
        return service.post('user/change/username', data).then(res => res)
    },
    uploadAvatar(data) {
        return service.post('user/upload/avatar', data).then(res => res)
    },

    // questionnaire
    createQuestionnaire(data) {
        return service.post('questionnaire/create', data).then(res => res)
    },
    getProjects(data) {
        return service.post('questionnaire/getProjects', data).then(res => res)
    },
    publishProject(data) {
        return service.post('questionnaire/publishProject', data).then(res => res)
    },
    suspendProject(data) {
        return service.post('questionnaire/suspendProject', data).then(res => res)
    },
    getProjectsCount() {
        return service.post('questionnaire/getProjectsCount').then(res => res)
    },
    getQuestion(data) {
        return service.post('questionnaire/getQuestion', data).then(res => res)
    },
    deleteQuestion(data) {
        return service.post('questionnaire/deleteQuestion', data).then(res => res)
    },
    moveQuestion(data) {
        return service.post('questionnaire/moveQuestion', data).then(res => res)
    },
    deleteProject(data) {
        return service.post('questionnaire/deleteProject', data).then(res => res)
    },
    createSingleChoice(data) {
        return service.post('questionnaire/createSingleChoice', data).then(res => res)
    },
    createMultipleChoice(data) {
        return service.post('questionnaire/createMultipleChoice', data).then(res => res)
    },
    createCompletion(data) {
        return service.post('questionnaire/createCompletion', data).then(res => res)
    },
    createImage(data) {
        return service.post('questionnaire/createImage', data).then(res => res)
    },

    editSingleChoice(data) {
        return service.post('questionnaire/editSingleChoice', data).then(res => res)
    },
    editMultipleChoice(data) {
        return service.post('questionnaire/editMultipleChoice', data).then(res => res)
    },
    editCompletion(data) {
        return service.post('questionnaire/editCompletion', data).then(res => res)
    },

    questionnaire: {
        getQuestionsPublic(data) {
            return service.post('questionnaire/getQuestionsPublic', data).then(res => res).catch(e => e)
        },
        getQuestionsPrivate(data) {
            return service.post('questionnaire/getQuestionsPrivate', data).then(res => res).catch(e => e)
        },
        postQuestionnaire(data) {
            return service.post('questionnaire/postQuestionnaire', data).then(res => res).catch(e => e)
        },

        getAnalysis(data) {
            return service.post('questionnaire/getAnalysis', data).then(res => res).catch(e => e)
        },
        getSubmits(data) {
            return service.post('questionnaire/getSubmits', data).then(res => res).catch(e => e)
        },
        getSubmitDetail(data) {
            return service.post('questionnaire/getSubmitDetail', data).then(res => res).catch(e => e)
        },
        downloadData(data) {
            return service.post('questionnaire/downloadData', data).then(res => res).catch(e => e)
        },
        deleteSubmit(data) {
            return service.post('questionnaire/deleteSubmit', data).then(res => res).catch(e => e)
        },
        getRecommendations(data) {
            return service.post('questionnaire/getRecommendations', data).then(res => res).catch(e => e)
        },
        searchProjects(data) {
            return service.post('questionnaire/searchProjects', data).then(res => res).catch(e => e)
        },
        getHotProjects(data) {
            return service.post('questionnaire/getHotProjects', data).then(res => res).catch(e => e)
        },
    }

}

export default api